# Generated by Django 5.1 on 2024-12-15 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_remove_carasoul_db_img2_remove_carasoul_db_img3_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cardmng_DB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cimg', models.ImageField(default='', upload_to='caimg')),
                ('Ctitle', models.CharField(default='', max_length=50)),
                ('Cdesc', models.CharField(default='', max_length=150)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
    ]
