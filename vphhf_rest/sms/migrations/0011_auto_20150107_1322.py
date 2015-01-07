# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0010_remove_document_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='checksum',
        ),
        migrations.AddField(
            model_name='document',
            name='md5sum',
            field=models.CharField(default=datetime.datetime(2015, 1, 7, 13, 22, 52, 233329, tzinfo=utc), max_length=36),
            preserve_default=False,
        ),
    ]
