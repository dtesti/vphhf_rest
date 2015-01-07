# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0002_auto_20141230_1750'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='is_encrypted',
            field=models.BooleanField(default=datetime.datetime(2015, 1, 7, 10, 56, 20, 294583, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
