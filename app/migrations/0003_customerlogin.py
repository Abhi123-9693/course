# Generated by Django 5.1 on 2024-09-01 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_customer_checkbox_customer_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customerlogin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_address', models.EmailField(max_length=225)),
                ('password', models.IntegerField(max_length=50)),
            ],
        ),
    ]
