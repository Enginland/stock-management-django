# Generated by Django 5.1.2 on 2024-11-01 13:44

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('quantity', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='StockTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_type', models.CharField(choices=[('IN', 'Stock In'), ('OUT', 'Stock Out')], max_length=3)),
                ('quantity', models.PositiveIntegerField()),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='inventory.stock')),
            ],
        ),
    ]