# Generated by Django 4.2 on 2023-11-30 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]