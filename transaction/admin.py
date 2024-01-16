from django.contrib import admin
from .models import Transaction

# admin.site.register(Transaction)

# @admin.register(Transaction)
# class TransactionAdmin(admin.ModelAdmin):
    # list_display = ['account',]
    
    # def save_model(self, request, obj, form, change):
    #     obj.account.balance += obj.amount 'amount'
    #     print("objaccount balance:", obj.account.balance)
    #     # obj.balance_after_transaction = obj.account.balance
    #     obj.account.save()
        