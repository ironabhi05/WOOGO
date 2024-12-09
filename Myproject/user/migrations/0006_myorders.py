# Generated by Django 3.2.4 on 2023-09-19 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20230919_1705'),
    ]

    operations = [
        migrations.CreateModel(
            name='myorders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=200, null=True)),
                ('product_name', models.CharField(max_length=200)),
                ('quantity', models.IntegerField(null=True)),
                ('price', models.IntegerField(null=True)),
                ('total_price', models.FloatField(null=True)),
                ('product_picture', models.CharField(max_length=300, null=True)),
                ('pw', models.CharField(max_length=200, null=True)),
                ('order_date', models.DateField()),
                ('status', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
