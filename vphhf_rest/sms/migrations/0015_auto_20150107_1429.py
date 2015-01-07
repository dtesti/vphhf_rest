# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0014_auto_20150107_1410'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='file_url',
            new_name='file_path',
        ),
    ]
