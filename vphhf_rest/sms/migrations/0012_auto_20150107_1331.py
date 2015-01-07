# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0011_auto_20150107_1322'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.FileField(upload_to=b'documents/%Y/%m/%d', verbose_name=b'file')),
                ('is_encrypted', models.BooleanField(default=None)),
                ('md5sum', models.CharField(max_length=36)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True, auto_now_add=True)),
            ],
            options={
                'ordering': ('created',),
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Document',
        ),
    ]
