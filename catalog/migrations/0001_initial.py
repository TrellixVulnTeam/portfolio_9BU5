# Generated by Django 2.0.3 on 2018-03-08 01:19

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index_title', models.TextField(blank=True, default=None, max_length=256, null=True, verbose_name='Заголовок на главной')),
                ('first_title', models.TextField(blank=True, default=None, max_length=256, null=True, verbose_name='Заголовок первого экрана')),
                ('first_text', tinymce.models.HTMLField(default=None, verbose_name='Текст на первом экране')),
                ('second_title', models.TextField(blank=True, default=None, max_length=256, null=True, verbose_name='Заголовок второго экрана')),
                ('third_title', models.TextField(blank=True, default=None, max_length=256, null=True, verbose_name='Заголовок экрана с консультацией')),
                ('meta_tags', models.TextField(blank=True, default=None, max_length=256, null=True, verbose_name='Мета теги страницы')),
                ('url_pretty', models.CharField(blank=True, default=None, max_length=256, null=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='CategoryCatalogImg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='static/img/categories', verbose_name='Фото каталога')),
                ('service', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.Category')),
            ],
            options={
                'verbose_name': 'Фото каталога',
                'verbose_name_plural': 'Фото каталога',
            },
        ),
        migrations.CreateModel(
            name='CategoryCatalogText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', tinymce.models.HTMLField(default=None, verbose_name='Пункт каталога')),
                ('service', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.Category')),
            ],
            options={
                'verbose_name': 'Пункт каталога',
                'verbose_name_plural': 'Пункты каталога',
            },
        ),
        migrations.CreateModel(
            name='CategoryConsImg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='static/img/categories', verbose_name='Фото консультация')),
                ('service', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.Category')),
            ],
            options={
                'verbose_name': 'Фото консультация',
                'verbose_name_plural': 'Фото консультации',
            },
        ),
        migrations.CreateModel(
            name='CategoryConsText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', tinymce.models.HTMLField(default=None, verbose_name='Пункт консултации')),
                ('service', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.Category')),
            ],
            options={
                'verbose_name': 'Пункт консултации',
                'verbose_name_plural': 'Пункты консултации',
            },
        ),
        migrations.CreateModel(
            name='CategoryIndexImg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='static/img/categories', verbose_name='Фото на главной')),
                ('service', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.Category')),
            ],
            options={
                'verbose_name': 'Фото на главной',
                'verbose_name_plural': 'Фото на главной',
            },
        ),
        migrations.CreateModel(
            name='CategoryInnerImg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='static/img/categories', verbose_name='Фото на первом экране')),
                ('service', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.Category')),
            ],
            options={
                'verbose_name': 'Фото на первом экране',
                'verbose_name_plural': 'Фото на первом экране',
            },
        ),
    ]
