# Generated by Django 5.0.2 on 2024-03-04 07:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financial', '0002_b2ctransaction_delete_b2btransaction'),
    ]

    operations = [
        migrations.CreateModel(
            name='STKpush',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('phone_number', models.CharField(max_length=100)),
                ('amount', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('received_at', models.DateTimeField(auto_now_add=True)),
                ('checkout_request_id', models.CharField(max_length=255)),
                ('merchant_request_id', models.CharField(max_length=255)),
                ('mpesa_receipt_no', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Transaction',
            },
        ),
    ]
