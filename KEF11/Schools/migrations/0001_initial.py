# Generated by Django 3.1 on 2020-08-08 07:16

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schools',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('headmaster', models.CharField(max_length=100)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employee')),
            ],
        ),
    ]
