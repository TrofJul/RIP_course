# Generated by Django 3.0.1 on 2019-12-25 20:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 25, 20, 19, 52, 532438, tzinfo=utc)),
        ),
    ]
