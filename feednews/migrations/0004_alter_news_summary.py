# Generated by Django 4.1 on 2022-08-18 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feednews', '0003_agency_datetime_format'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='summary',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
