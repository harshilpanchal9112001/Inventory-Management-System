# Generated by Django 4.2 on 2023-05-22 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminPanel', '0014_alter_productmodel_productdesc_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='quantity_sold',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
