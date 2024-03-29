# Generated by Django 4.2.6 on 2024-02-17 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('english', '0006_alter_sourcemodel_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wordmodel',
            name='word_count',
            field=models.CharField(choices=[('NC', 'Любое количество слов'), ('OW', 'Слово'), ('CB', 'Словосочетание'), ('PS', 'Часть предложения'), ('ST', 'Предложение')], default=('NC', 'Любое количество слов'), max_length=2, verbose_name='Количество слов'),
        ),
    ]
