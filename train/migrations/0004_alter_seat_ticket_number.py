# Generated by Django 4.2.7 on 2024-01-15 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('train', '0003_alter_seat_ticket_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seat',
            name='ticket_number',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9')], default=['1', '2', '3', '4', '5', '6', '7', '8', '9'], max_length=1),
        ),
    ]
