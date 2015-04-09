# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('header', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone1', models.CharField(max_length=20, verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xbb\xd0\xb5\xd1\x84\xd0\xbe\xd0\xbd 1')),
                ('phone2', models.CharField(max_length=20, verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xbb\xd0\xb5\xd1\x84\xd0\xbe\xd0\xbd 2')),
            ],
            options={
                'db_table': 'contacts',
                'verbose_name': '\u041a\u043e\u043d\u0442\u0430\u043a\u0442\u044b',
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='logo',
            options={'verbose_name': '\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0441\u0430\u0439\u0442\u0430'},
        ),
    ]
