# Generated by Django 3.0.5 on 2020-04-20 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_auto_20200420_1904'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AddField(
            model_name='recipe',
            name='image_path',
            field=models.CharField(blank=True, max_length=210, null=True),
        ),
        migrations.AddIndex(
            model_name='recipe',
            index=models.Index(fields=['slug'], name='recipes_rec_slug_412256_idx'),
        ),
        migrations.AddIndex(
            model_name='recipe',
            index=models.Index(fields=['rating'], name='recipes_rec_rating_e9153a_idx'),
        ),
    ]
