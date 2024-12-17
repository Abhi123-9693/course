# Generated by Django 5.1 on 2024-12-13 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_freeread_db_des_freeread_db_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_db',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=225)),
                ('pbrand', models.CharField(max_length=225)),
                ('pprice', models.IntegerField(max_length=225)),
                ('psellprice', models.IntegerField(max_length=225)),
                ('pdiscount', models.IntegerField(max_length=225)),
                ('pimage', models.ImageField(blank=True, default=None, null=True, upload_to='img')),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
