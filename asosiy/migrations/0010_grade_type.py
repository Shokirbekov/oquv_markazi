# Generated by Django 4.2.1 on 2023-08-01 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asosiy', '0009_lessonprofile_klass'),
    ]

    operations = [
        migrations.AddField(
            model_name='grade',
            name='type',
            field=models.CharField(choices=[('Lesson', 'Lesson'), ('Homework', 'Homework')], max_length=200, null=True),
        ),
    ]
