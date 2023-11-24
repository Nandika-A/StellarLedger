from django.db import models
from django.contrib.auth.models import User
from collections import defaultdict
from heapq import heappush, heappop

class ExpenseGroup(models.Model):
    name = models.CharField(max_length=10, unique=True, default="GroupX")
    description = models.TextField(blank=True, null=True)

class ExpenseGroupMember(models.Model):
    group = models.ForeignKey(ExpenseGroup, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Edge(models.Model):
    group = models.ForeignKey(ExpenseGroup, on_delete=models.CASCADE, default=1)
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
        self.N = len(self.members)
        self.member_id_to_index = {}
        self.index_to_member_id = {}

    def set_member_id(self):
        a = 0
        for m in self.members:
            self.member_id_to_index[m.id] = a
            self.index_to_member_id[a] = m.id
            a += 1


    def create_edges(self):
        graph = [[0 for i in range(self.N)] for j in range(self.N)]
        self.set_member_id()
        for edge in self.group.edge_set.all():
            graph[self.member_id_to_index[edge.debtor.id]][self.member_id_to_index[edge.creditor.id]] += edge.amount
        self.minimize_cash_flow(graph) 

    def getMin(self,arr):
        minInd = 0
        for i in range(1, self.N):
            if (arr[i] < arr[minInd]):
                minInd = i
        return minInd
    
    def getMax(self,arr):
        maxInd = 0
        for i in range(1, self.N):
            if (arr[i] > arr[maxInd]):
                maxInd = i
        return maxInd
    
    def minCashFlowRec(self, amount):
        mxCredit = self.getMax(amount)
        mxDebit = self.getMin(amount)
        if (amount[mxCredit] == 0 and amount[mxDebit] == 0):
            return 0
        if -amount[mxDebit] < amount[mxCredit]:
            min = -amount[mxDebit]
        else:
            min = amount[mxCredit]
        amount[mxCredit] -=min
        amount[mxDebit] += min
        
        self.transactions.append({
            'debtor' : self.index_to_member_id[mxDebit],
            'creditor': self.index_to_member_id[mxCredit],
            'amount': min
            })

        self.minCashFlowRec(amount)

    def minimize_cash_flow(self, graph):
        amount = [0 for i in range(self.N)]
        for p in range(self.N):
            for i in range(self.N):
                amount[p] += (graph[i][p] - graph[p][i])
                # print(f'{p}, {i}, {graph[p][i]}')
            # print(amount[p])
        self.minCashFlowRec(amount)


    def get_transactions(self):
        return self.transactions