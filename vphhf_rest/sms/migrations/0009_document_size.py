# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0008_auto_20150107_1145'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='size',
            field=models.IntegerField(default=10),
            preserve_default=True,
        ),
    ]
