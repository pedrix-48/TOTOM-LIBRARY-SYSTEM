# Generated by Django 5.0.7 on 2025-05-26 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0008_admin_user_password_admin_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudante',
            name='foto_profile',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='estudante',
            name='nre',
            field=models.CharField(max_length=11, primary_key=True, serialize=False, unique=True),
        ),
    ]
