# Generated by Django 4.1 on 2022-08-17 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feednews', '0002_agency_news_agency'),
    ]

    operations = [
        migrations.AddField(
            model_name='agency',
            name='datetime_format',
            field=models.CharField(default='%Y-%m-%dT%H:%M:%S', max_length=1000),
            preserve_default=False,
        ),
    ]
