# Generated by Django 3.1.6 on 2021-02-15 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App2', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='Date_Of_Birth',
            field=models.DateField(null=True),
        ),
    ]
