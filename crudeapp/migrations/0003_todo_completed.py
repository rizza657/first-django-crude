# Generated by Django 5.1.1 on 2024-09-19 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudeapp', '0002_rename_name_todo_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
