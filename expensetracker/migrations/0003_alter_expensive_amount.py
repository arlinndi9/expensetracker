# Generated by Django 5.0.1 on 2024-01-30 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expensetracker', '0002_remove_expensive_balance_remove_expensive_expense_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expensive',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
