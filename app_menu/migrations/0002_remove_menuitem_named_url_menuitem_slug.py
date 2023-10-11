# Generated by Django 4.2.6 on 2023-10-10 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_menu', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='named_url',
        ),
        migrations.AddField(
            model_name='menuitem',
            name='slug',
            field=models.SlugField(default='slug_text'),
            preserve_default=False,
        ),
    ]