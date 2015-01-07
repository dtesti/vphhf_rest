# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0005_auto_20150107_1102'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='checksum',
            field=models.TextField(default=b'pincopallo'),
            preserve_default=True,
        ),
    ]
