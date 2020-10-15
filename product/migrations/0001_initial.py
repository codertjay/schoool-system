# Generated by Django 3.0.7 on 2020-07-02 21:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('quantity', models.IntegerField(blank=True, default=1, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('digital', models.BooleanField(default=False)),
                ('product_accessory', models.CharField(blank=True, choices=[('S', 'SHIRT'), ('SW', 'Sport wear'), ('Ow', 'Out Wear'), ('ba', 'Bag'), ('Fu', 'Furniture'), ('Bo', 'Book'), ('La', 'Laptop'), ('Ph', 'Phone'), ('Ca', 'Camera'), ('Ch', 'Charger'), ('He', 'Headset'), ('Mo', 'Mouse')], max_length=5, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('discount_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('time_stamp', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('time_stamp', models.DateField(auto_now_add=True)),
                ('ordered', models.BooleanField(default=False)),
                ('products', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Product')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered', models.BooleanField(default=False)),
                ('ordered_date', models.DateField(auto_now_add=True)),
                ('transaction_id', models.CharField(blank=True, max_length=50, null=True)),
                ('products', models.ManyToManyField(to='product.OrderItem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]