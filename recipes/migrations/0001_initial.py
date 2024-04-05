# Generated by Django 3.0.5 on 2020-04-20 03:32

import django.contrib.postgres.fields
import django.contrib.postgres.indexes
import django.contrib.postgres.search
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cuisine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('total_time', models.IntegerField()),
                ('servings', models.CharField(max_length=100)),
                ('rating', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField()),
                ('ingredients', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=1500), size=None)),
                ('search_vector', django.contrib.postgres.search.SearchVectorField(null=True)),
                ('categories', models.ManyToManyField(to='recipes.Category')),
                ('cuisine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.Cuisine')),
            ],
        ),
        migrations.AddIndex(
            model_name='recipe',
            index=django.contrib.postgres.indexes.GinIndex(fields=['search_vector'], name='recipes_rec_search__ce256b_gin'),
        ),
    ]