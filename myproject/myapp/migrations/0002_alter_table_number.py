# Generated by Django 5.1.6 on 2025-02-10 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='number',
            field=models.PositiveIntegerField(unique=True),
        ),
    ]
