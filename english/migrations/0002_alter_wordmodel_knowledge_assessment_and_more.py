# Generated by Django 4.2.6 on 2024-01-10 10:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('english', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wordmodel',
            name='knowledge_assessment',
            field=models.ManyToManyField(blank=True, related_name='word_knowledge', through='english.WordUserKnowledgeRelation', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='WordsFavoritesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('word', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='english.wordmodel')),
            ],
        ),
        migrations.AddField(
            model_name='wordmodel',
            name='favorites',
            field=models.ManyToManyField(blank=True, related_name='word_favorites', through='english.WordsFavoritesModel', to=settings.AUTH_USER_MODEL),
        ),
    ]
