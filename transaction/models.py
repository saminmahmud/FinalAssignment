from django.db import models
from passenger.models import UserAccount

class Transaction(models.Model):
    account = models.ForeignKey(UserAccount, on_delete=models.CASCADE, null=True, blank=True)
    # amount = models.DecimalField(decimal_places=2, max_digits=12)

