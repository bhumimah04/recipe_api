# Generated by Django 3.0.5 on 2020-04-21 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_recipe_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='cuisine',
        ),
    ]
