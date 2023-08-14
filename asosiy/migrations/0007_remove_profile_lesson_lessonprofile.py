# Generated by Django 4.2.1 on 2023-08-01 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asosiy', '0006_remove_profile_lesson_profile_lesson'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='lesson',
        ),
        migrations.CreateModel(
            name='LessonProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lesson_info', to='asosiy.lesson')),
                ('profil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.profile')),
            ],
        ),
    ]
