# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import vphhf_rest.sms.models


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0012_auto_20150107_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='url',
            field=models.FileField(upload_to=b'documents/%Y/%m/%d', storage=vphhf_rest.sms.models.MediaFileSystemStorage(), verbose_name=b'file'),
            preserve_default=True,
        ),
    ]
