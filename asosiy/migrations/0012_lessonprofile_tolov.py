# Generated by Django 4.2.1 on 2023-08-02 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asosiy', '0011_tolov'),
    ]

    operations = [
        migrations.AddField(
            model_name='lessonprofile',
            name='tolov',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tolov_info', to='asosiy.tolov'),
        ),
    ]
