# Generated by Django 4.2.6 on 2024-01-11 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('english', '0004_alter_wordsfavoritesmodel_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categorymodel',
            options={'ordering': ['name'], 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
    ]
