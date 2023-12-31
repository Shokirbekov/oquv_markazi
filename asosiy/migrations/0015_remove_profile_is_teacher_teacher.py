# Generated by Django 4.2.4 on 2023-08-11 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asosiy', '0014_profile_is_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='is_teacher',
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('lessons', models.ManyToManyField(to='asosiy.lesson')),
                ('profil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.profile')),
            ],
        ),
    ]
