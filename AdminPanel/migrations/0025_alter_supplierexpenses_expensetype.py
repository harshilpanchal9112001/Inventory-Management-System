# Generated by Django 4.2 on 2023-06-04 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminPanel', '0024_supplierexpenses_expensetype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplierexpenses',
            name='expenseType',
            field=models.CharField(max_length=100),
        ),
    ]
