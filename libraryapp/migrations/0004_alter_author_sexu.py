# Generated by Django 5.0.7 on 2025-05-08 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0003_alter_author_sexu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='sexu',
            field=models.CharField(choices=[('Mane', 'Mane'), ('Feto', 'Feto')], max_length=4),
        ),
    ]
