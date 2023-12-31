# Generated by Django 4.2.6 on 2024-01-07 14:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Наименование категории')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='LabelModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Наименование метки')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Метка',
                'verbose_name_plural': 'Метки',
            },
        ),
        migrations.CreateModel(
            name='LessonModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Тема урока')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Урок',
                'verbose_name_plural': 'Уроки',
            },
        ),
        migrations.CreateModel(
            name='SourceModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Не более 50 символов', max_length=50, verbose_name='Источник')),
                ('url', models.URLField(blank=True, max_length=255, null=True, verbose_name='Ссылка')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Источник',
                'verbose_name_plural': 'Источники',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='WordLabelRelation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='english.labelmodel')),
            ],
        ),
        migrations.CreateModel(
            name='WordModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('words_eng', models.CharField(max_length=75, verbose_name='Слово на английском')),
                ('words_rus', models.CharField(max_length=75, verbose_name='Слово на русском')),
                ('word_count', models.CharField(choices=[('NC', 'Любое количество слов'), ('OW', 'Слово'), ('CB', 'Словосочетание'), ('PS', 'Часть предложения'), ('ST', 'Предложение')], default='NC', max_length=2, verbose_name='Количество слов')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='english.categorymodel', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Англо-русский словарь',
                'verbose_name_plural': 'Англо-русский словарь',
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='WordUserKnowledgeRelation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('knowledge_assessment', models.DecimalField(decimal_places=0, default=0, max_digits=2)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('word', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='english.wordmodel')),
            ],
        ),
        migrations.AddField(
            model_name='wordmodel',
            name='knowledge_assessment',
            field=models.ManyToManyField(blank=True, through='english.WordUserKnowledgeRelation', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='wordmodel',
            name='labels',
            field=models.ManyToManyField(blank=True, related_name='labels', through='english.WordLabelRelation', to='english.labelmodel', verbose_name='Метки'),
        ),
        migrations.AddField(
            model_name='wordmodel',
            name='lesson',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='english.lessonmodel', verbose_name='Тема урока'),
        ),
        migrations.AddField(
            model_name='wordmodel',
            name='source',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='get_source', to='english.sourcemodel', verbose_name='Источник'),
        ),
        migrations.AddField(
            model_name='wordmodel',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vocabulary_added_by_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='wordlabelrelation',
            name='word',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='english.wordmodel'),
        ),
    ]
