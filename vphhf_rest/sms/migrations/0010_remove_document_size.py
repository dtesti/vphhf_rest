# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0009_document_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='size',
        ),
    ]
