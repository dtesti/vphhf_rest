# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 30, 17, 50, 17, 571724, tzinfo=utc), auto_now=True, auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='document',
            name='url',
            field=models.FileField(upload_to=b'documents/%Y/%m/%d', verbose_name=b'file'),
            preserve_default=True,
        ),
    ]
