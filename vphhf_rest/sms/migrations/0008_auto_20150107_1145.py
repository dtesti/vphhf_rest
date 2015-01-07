# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0007_auto_20150107_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='checksum',
            field=models.TextField(default=b'pincopallo'),
            preserve_default=True,
        ),
    ]
