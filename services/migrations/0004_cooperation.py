# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_uservices'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cooperation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField(verbose_name=b'\xd0\x92\xd0\xb0\xd1\x88 \xd0\xa2\xd0\xb5\xd0\xba\xd1\x81\xd1\x82')),
            ],
            options={
                'db_table': 'cooperation',
                'verbose_name': '\u0421\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u0447\u0435\u0441\u0442\u0432\u043e',
                'verbose_name_plural': '\u0421\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u0447\u0435\u0441\u0442\u0432\u043e',
            },
            bases=(models.Model,),
        ),
    ]
