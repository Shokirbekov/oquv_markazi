# Generated by Django 4.2.4 on 2023-08-11 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asosiy', '0013_tolov_is_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_teacher',
            field=models.BooleanField(default=False),
        ),
    ]