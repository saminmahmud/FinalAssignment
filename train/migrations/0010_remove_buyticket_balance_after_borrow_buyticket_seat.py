# Generated by Django 4.2.7 on 2024-01-15 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('train', '0009_remove_train_seat_seat_train'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buyticket',
            name='balance_after_borrow',
        ),
        migrations.AddField(
            model_name='buyticket',
            name='seat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='train.seat'),
        ),
    ]