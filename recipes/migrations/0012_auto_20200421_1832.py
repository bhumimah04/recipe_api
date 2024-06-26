# Generated by Django 3.0.5 on 2020-04-21 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0011_auto_20200421_1831'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='rating_count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddIndex(
            model_name='recipe',
            index=models.Index(fields=['rating_count'], name='recipes_rec_rating__66f33e_idx'),
        ),
    ]
