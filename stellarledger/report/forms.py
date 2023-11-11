from django.forms import ModelForm
from .models import Transaction, Category

class RecordTransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = ['to_or_from','user_role', 'amount', 'timestamp', 'category', 'recurring']
        labels = {
            "recurring": _('Bill paid?'),
        }

class RecordCategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['category']