# Generated by Django 3.2.4 on 2023-09-19 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=200, null=True)),
                ('product_name', models.CharField(max_length=200)),
                ('quantity', models.CharField(max_length=200)),
                ('price', models.IntegerField(null=True)),
                ('total_price', models.FloatField()),
                ('product_picture', models.CharField(max_length=300, null=True)),
                ('pw', models.CharField(max_length=200, null=True)),
                ('added_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=200, null=True)),
                ('cpic', models.ImageField(null=True, upload_to='static/category')),
                ('cdate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200, null=True)),
                ('Email', models.CharField(max_length=100, null=True)),
                ('Mobile', models.CharField(max_length=25, null=True)),
                ('Message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='register',
            fields=[
                ('name', models.CharField(max_length=150, null=True)),
                ('email', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('mobile', models.CharField(max_length=30, null=True)),
                ('passwd', models.CharField(max_length=100, null=True)),
                ('profile', models.ImageField(null=True, upload_to='static/userpic/')),
                ('address', models.CharField(max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spic', models.ImageField(null=True, upload_to='static/slider')),
                ('sdate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcategory_name', models.CharField(max_length=100, null=True)),
                ('category_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.category')),
            ],
        ),
        migrations.CreateModel(
            name='myproduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('discount_price', models.IntegerField()),
                ('product_pic', models.ImageField(null=True, upload_to='static/product/')),
                ('total_discount', models.IntegerField()),
                ('product_quantity', models.CharField(max_length=200)),
                ('pdate', models.DateField()),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.category')),
                ('subcategory_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.subcategory')),
            ],
        ),
    ]