# Generated by Django 3.1 on 2020-08-08 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_employee_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('useremail', models.EmailField(max_length=254)),
                ('is_super', models.BooleanField(default=False)),
            ],
        ),
    ]
