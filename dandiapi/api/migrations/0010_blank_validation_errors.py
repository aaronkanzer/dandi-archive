# Generated by Django 3.2 on 2021-06-28 22:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('api', '0009_asset_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='validation_error',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='version',
            name='validation_error',
            field=models.TextField(blank=True, default=''),
        ),
    ]
