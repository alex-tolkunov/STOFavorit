# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TabItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
            ],
            options={
                'db_table': 'tab_item',
                'verbose_name': '\u0422\u0430\u0431',
                'verbose_name_plural': '\u0422\u0430\u0431\u044b',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TabItemList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item', models.TextField(verbose_name=b'\xd0\xa1\xd0\xbe\xd0\xb4\xd0\xb5\xd1\x80\xd0\xb6\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd1\x82\xd0\xb0\xd0\xb1\xd0\xb0')),
                ('link', models.URLField(verbose_name=b'\xd0\xa1\xd1\x81\xd1\x8b\xd0\xbb\xd0\xba\xd0\xb0')),
                ('tab', models.ForeignKey(to='PanelTabs.TabItem')),
            ],
            options={
                'db_table': 'tab_item_list',
                'verbose_name': '\u0422\u0430\u0431',
                'verbose_name_plural': '\u0422\u0430\u0431\u044b',
            },
            bases=(models.Model,),
        ),
    ]
