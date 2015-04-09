# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name=b'\xd0\x97\xd0\xb0\xd0\xb3\xd0\xbe\xd0\xbb\xd0\xbe\xd0\xb2\xd0\xbe\xd0\xba')),
                ('city', models.CharField(max_length=20, verbose_name=b'\xd0\x93\xd0\xbe\xd1\x80\xd0\xbe\xd0\xb4')),
            ],
            options={
                'db_table': 'logo',
                'verbose_name': '\u041b\u043e\u0433\u043e\u0442\u0438\u043f',
            },
            bases=(models.Model,),
        ),
    ]
