# Generated by Django 3.2.6 on 2021-08-28 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1994-12-20'),
            preserve_default=False,
        ),
    ]
