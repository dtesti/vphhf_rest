# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0015_auto_20150107_1429'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='file_path',
            new_name='url',
        ),
    ]
