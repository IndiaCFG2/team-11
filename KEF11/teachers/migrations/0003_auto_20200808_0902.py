# Generated by Django 3.1 on 2020-08-08 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0002_auto_20200808_0857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachers',
            name='college',
            field=models.CharField(max_length=100),
        ),
    ]
