# Generated by Django 4.2.6 on 2023-12-19 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('english', '0005_labelmodel_created_at_labelmodel_updated_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='labelmodel',
            options={'verbose_name': 'Метка', 'verbose_name_plural': 'Метки'},
        ),
    ]