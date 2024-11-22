# Generated by Django 4.2.15 on 2024-11-06 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='has_responded',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='notification',
            name='notif_type',
            field=models.CharField(choices=[('invite', 'Invitation'), ('remove', 'Removed'), ('accepted', 'Accepted'), ('declined', 'Declined')], max_length=10),
        ),
    ]
