# Generated by Django 4.2.6 on 2024-02-20 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('english', '0012_alter_wordmodel_lesson'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wordmodel',
            name='lesson',
        ),
        migrations.DeleteModel(
            name='LessonModel',
        ),
    ]
