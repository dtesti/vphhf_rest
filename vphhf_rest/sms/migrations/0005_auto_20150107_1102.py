# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0004_auto_20150107_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='is_encrypted',
            field=models.BooleanField(default=None),
            preserve_default=True,
        ),
    ]
