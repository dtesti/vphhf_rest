# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0017_auto_20150107_1443'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='purl',
            new_name='url',
        ),
    ]
