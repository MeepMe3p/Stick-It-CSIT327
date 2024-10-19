# Generated by Django 5.1.2 on 2024-10-13 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('border_color', models.CharField(max_length=10)),
                ('coordinates', models.JSONField()),
                ('is_finished', models.BooleanField(default=False)),
                ('checkbox_id', models.CharField(max_length=100)),
            ],
        ),
    ]
