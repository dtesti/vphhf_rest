# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import vphhf_rest.sms.models


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0020_auto_20150107_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='filepath',
            field=models.FileField(help_text=b'Browse a file', upload_to=b'documents/%Y/%m/%d', storage=vphhf_rest.sms.models.MediaFileSystemStorage(), verbose_name=b'file'),
            preserve_default=True,
        ),
    ]
