# Generated by Django 4.2 on 2023-05-22 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminPanel', '0013_productmodel_quantity_sold'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='productdesc',
            field=models.CharField(default='Not set', max_length=900, null=True),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='quantity_sold',
            field=models.IntegerField(null=True),
        ),
    ]
