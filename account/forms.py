from django.forms import ModelForm

from account.models import Transaction


class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = ['amount', 'sender','recipient']