# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0006_document_checksum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='checksum',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]
