# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_cooperation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cooperation',
            name='text',
            field=models.TextField(verbose_name=b'\xd0\x92\xd0\xb0\xd1\x88 \xd1\x82\xd0\xb5\xd0\xba\xd1\x81\xd1\x82'),
            preserve_default=True,
        ),
    ]
