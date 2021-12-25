# Generated by Django 2.2.17 on 2021-12-25 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('circles', '0002_auto_20211225_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Only active users are allowed to interact in the circle.', verbose_name='active status'),
        ),
        migrations.AlterField(
            model_name='membership',
            name='is_admin',
            field=models.BooleanField(default=False, help_text="Circle admins can update the circle's data and manage its members.", verbose_name='circle admin'),
        ),
    ]
