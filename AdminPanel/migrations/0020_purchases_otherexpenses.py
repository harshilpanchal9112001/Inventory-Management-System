# Generated by Django 4.2 on 2023-06-01 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminPanel', '0019_purchases_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchases',
            name='otherExpenses',
            field=models.FloatField(default=0.0),
        ),
    ]
