# Generated by Django 3.1.4 on 2021-04-19 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('air', '0003_send_feedback_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='send_feedback',
            name='date',
            field=models.DateField(blank=True, max_length=100, null=True),
        ),
    ]
