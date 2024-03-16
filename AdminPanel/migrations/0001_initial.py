# Generated by Django 4.2 on 2023-04-26 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminLogin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.AutoField(default=0, primary_key=True, serialize=False)),
                ('categoryname', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productid', models.IntegerField(default=0, null=True)),
                ('productname', models.CharField(default='Not set', max_length=100)),
                ('productsize', models.IntegerField(default=0, null=True)),
                ('productcolor', models.CharField(default='Not set', max_length=100)),
                ('productmaterial', models.CharField(default='Not set', max_length=100)),
                ('productprice', models.IntegerField(default=0, null=True)),
                ('productstock', models.IntegerField(default=0, null=True)),
                ('productdesc', models.CharField(default='Not set', max_length=900)),
                ('productimage', models.ImageField(default='static/assets/images/product-images/shirt.png', upload_to='static/assets/images/product-images/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminPanel.categorymodel')),
            ],
        ),
    ]
