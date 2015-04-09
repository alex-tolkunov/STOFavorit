# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_auto_20150408_2023'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='uservices',
            options={'verbose_name': '\u0421\u043f\u0438\u0441\u043e\u043a \u0443\u0441\u043b\u0443\u0433', 'verbose_name_plural': '\u0421\u043f\u0438\u0441\u043e\u043a \u0443\u0441\u043b\u0443\u0433'},
        ),
        migrations.AddField(
            model_name='uservices',
            name='measure',
            field=models.CharField(default=None, choices=[(None, b'\xd0\x9d\xd0\xb5\xd1\x82'), (b'\xd0\xa7\xd0\xb0\xd1\x81', b'\xd0\xa7\xd0\xb0\xd1\x81'), (b'\xd0\xad\xd1\x82\xd0\xb0\xd0\xb6', b'\xd0\xad\xd1\x82\xd0\xb0\xd0\xb6'), (b'\xd0\x9a\xd0\xb2.\xd0\xbc\xd0\xb5\xd1\x82\xd1\x80', b'\xd0\x9a\xd0\xb2.\xd0\xbc\xd0\xb5\xd1\x82\xd1\x80'), (b'\xd0\xa2\xd0\xbe\xd1\x87\xd0\xba\xd0\xb0', b'\xd0\xa2\xd0\xbe\xd1\x87\xd0\xba\xd0\xb0'), (b'\xd0\xa8\xd1\x82', b'\xd0\xa8\xd1\x82'), (b'\xd0\x9a\xd0\xb3', b'\xd0\x9a\xd0\xb3'), (b'\xd0\x9b\xd0\xb8\xd1\x82\xd1\x80', b'\xd0\x9b\xd0\xb8\xd1\x82\xd1\x80')], max_length=10, blank=True, null=True, verbose_name=b'\xd0\x95\xd0\xb4. \xd0\xb8\xd0\xb7\xd0\xbc\xd0\xb5\xd1\x80\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='uservices',
            name='note',
            field=models.CharField(max_length=b'255', null=True, verbose_name=b'\xd0\x9f\xd1\x80\xd0\xb8\xd0\xbc\xd0\xb5\xd1\x87\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5', blank=True),
            preserve_default=True,
        ),
    ]
