# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_service_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='UServices',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
                ('price', models.CharField(max_length=20, verbose_name=b'\xd0\xa6\xd0\xb5\xd0\xbd\xd0\xb0')),
                ('changed', models.BooleanField(default=False, verbose_name=b'\xd0\x92\xd1\x8b\xd0\xb1\xd1\x80\xd0\xb0\xd1\x82\xd1\x8c \xd1\x83\xd1\x81\xd0\xbb\xd1\x83\xd0\xb3\xd1\x83')),
                ('service', models.ForeignKey(to='services.Service')),
            ],
            options={
                'db_table': 'uservices',
                'verbose_name': '\u0423\u0441\u043b\u0443\u0433\u0430',
                'verbose_name_plural': '\u0423\u0441\u043b\u0443\u0433\u0438',
            },
            bases=(models.Model,),
        ),
    ]
