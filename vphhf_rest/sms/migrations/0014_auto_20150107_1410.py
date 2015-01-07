# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0013_auto_20150107_1345'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='url',
            new_name='file_url',
        ),
    ]
