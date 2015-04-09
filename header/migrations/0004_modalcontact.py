# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('header', '0003_auto_20150407_2034'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModalContact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone1', models.CharField(max_length=20, verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xbb\xd0\xb5\xd1\x84\xd0\xbe\xd0\xbd 1')),
                ('phone2', models.CharField(max_length=20, verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xbb\xd0\xb5\xd1\x84\xd0\xbe\xd0\xbd 2')),
                ('email', models.EmailField(max_length=75, verbose_name=b'E-mail')),
            ],
            options={
                'db_table': 'contacts_modal',
                'verbose_name': '\u041a\u043e\u043d\u0442\u0430\u043a\u0442\u044b \u041c\u043e\u0434\u0430\u043b\u044c\u043d\u043e\u0435 \u043e\u043a\u043d\u043e',
                'verbose_name_plural': '\u041a\u043e\u043d\u0442\u0430\u043a\u0442\u044b \u041c\u043e\u0434\u0430\u043b\u044c\u043d\u043e\u0435 \u043e\u043a\u043d\u043e',
            },
            bases=(models.Model,),
        ),
    ]
