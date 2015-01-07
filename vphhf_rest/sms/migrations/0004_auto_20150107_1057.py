# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0003_document_is_encrypted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='is_encrypted',
            field=models.BooleanField(null=None),
            preserve_default=True,
        ),
    ]
