from django.db import models
from django.contrib.auth.models import User
from collections import defaultdict
from heapq import heappush, heappop

class ExpenseGroup(models.Model):
    name = models.CharField(max_length=10, unique=True)
    description = models.TextField(blank=True, null=True)

class ExpenseGroupMember(models.Model):
    group = models.ForeignKey(ExpenseGroup, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class ExpenseGraph(models.Model):
    group = models.OneToOneField(ExpenseGroup, on_delete=models.CASCADE)

class Edge(models.Model):
    graph = models.ForeignKey(ExpenseGraph, on_delete=models.CASCADE)
    debtor = models.ForeignKey(ExpenseGroupMember, related_name='debtor', on_delete=models.CASCADE)
    creditor = models.ForeignKey(ExpenseGroupMember, related_name='creditor', on_delete=models.CASCADE)
    amount = models.DecimalField(default=0.00, decimal_places=2, max_digits=10, blank=True)
    title = models.CharField(max_length=10)

class ExpenseGraphSolver:
    def __init__(self, group):
        self.group = group
        self.members = list(group.expensegroupmember_set.all())
        self.edges = defaultdict(list)
        self.transactions = []

    def add_edge(self, debtor, creditor, amount, title):
        self.edges[debtor].append({'creditor': creditor, 'amount': amount, 'title': title})

    def create_edges(self):
        for edge in self.group.edge_set.all():
            debtor = edge.debtor
            creditor = edge.creditor
            amount = edge.amount
            title = edge.title
            self.add_edge(debtor, creditor, amount, title)

    def minimize_cash_flow(self):
        debtors = self.members.copy()
        creditors = self.members.copy()
        debts = []
        
        for debtor in debtors:
            for creditor_info in self.edges[debtor]:
                creditor = creditor_info['creditor']
                amount = creditor_info['amount']
                title = creditor_info['title']
                debts.append((debtor, creditor, amount, title))

        debts.sort(key=lambda x: x[2])
        debtor_heap = []
        creditor_heap = []
        
        for debtor, creditor, amount, title in debts:
            if amount > 0:
                heappush(debtor_heap, (amount, debtor, creditor, title))
            else:
                heappush(creditor_heap, (-amount, creditor, debtor, title))

        while debtor_heap and creditor_heap:
            amount, debtor, creditor, title = heappop(debtor_heap)
            amount_c, creditor_c, debtor_c, title_c = heappop(creditor_heap)

            min_amount = min(amount, amount_c)

            amount -= min_amount
            amount_c += min_amount

            self.transactions.append({
                'debtor_username': debtor.user.username,
                'creditor_username': creditor.user.username,
                'amount': min_amount,
                'title': title
            })

            if amount > 0:
                heappush(debtor_heap, (amount, debtor, creditor, title))

            if amount_c > 0:
                heappush(creditor_heap, (-amount_c, creditor, debtor, title_c))
    
    def get_transactions(self):
        return self.transactions