# Generated by Django 5.0.7 on 2025-05-08 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='sexu',
            field=models.CharField(choices=[('Mane', 'Mane'), ('Feto', 'Feto')], max_length=4),
        ),
    ]
