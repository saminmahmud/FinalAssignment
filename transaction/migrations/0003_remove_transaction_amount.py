# Generated by Django 4.2.7 on 2024-01-15 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0002_remove_transaction_balance_after_transaction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='amount',
        ),
    ]