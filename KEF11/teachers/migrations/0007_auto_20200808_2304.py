# Generated by Django 3.1 on 2020-08-08 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0006_query_reply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='reply',
            field=models.TextField(default='', help_text="Please don't exceed 450 characters.", max_length=1000),
        ),
    ]