from django.shortcuts import render
from passenger.models import UserAccount
from django.views.generic import CreateView, ListView
from .models import Transaction
from django.urls import reverse_lazy
from .forms import DepositForm

class DepositeMoney(CreateView):
    model = Transaction
    form_class = DepositForm
    template_name = 'deposite.html'
    success_url = reverse_lazy('deposite') 
    
    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')
        account = self.request.user.account
        
        initial_balance = account.balance
        new_balance = initial_balance + amount

        print(f"amount: {amount}")
        print(f"NID: {account.nid}")
        print(f"initial_balance: {initial_balance}")
        print(f"new_balance: {new_balance}")

        print(f"HIiiii samin")

        account.balance = new_balance
        print(f"new_balance: {account.balance}")
        account.save(update_fields=['balance'])

        
        return super().form_valid(form)
      