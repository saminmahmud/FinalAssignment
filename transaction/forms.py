from .models import Transaction
from django import forms

class DepositForm(forms.ModelForm):
    amount = forms.DecimalField(decimal_places=2, max_digits=12)
    class Meta:
        model = Transaction
        fields = [
            'amount'
        ]
        