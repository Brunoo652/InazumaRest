# Generated by Django 4.1.2 on 2023-04-17 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InazumaApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stat',
            name='valor',
            field=models.IntegerField(),
        ),
    ]
