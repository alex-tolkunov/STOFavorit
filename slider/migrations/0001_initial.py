# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SlideHead',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name=b'\xd0\x97\xd0\xb0\xd0\xb3\xd0\xbe\xd0\xbb\xd0\xbe\xd0\xb2\xd0\xbe\xd0\xba')),
                ('photo', models.CharField(max_length=100, verbose_name=b'\xd0\x98\xd0\xb7\xd0\xbe\xd0\xb1\xd1\x80\xd0\xb0\xd0\xb6\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5')),
            ],
            options={
                'db_table': 'slider_head',
                'verbose_name': '\u0421\u043b\u0430\u0439\u0434',
                'verbose_name_plural': '\u0421\u043b\u0430\u0439\u0434\u0435\u0440 Header',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SlideList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('list', models.CharField(max_length=255, verbose_name=b'\xd0\x9e\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
                ('slide', models.ForeignKey(to='slider.SlideHead')),
            ],
            options={
                'db_table': 'slider_list',
                'verbose_name': '\u0421\u043f\u0438\u0441\u043e\u043a \u0441 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u044f\u043c\u0438',
                'verbose_name_plural': '\u0421\u043f\u0438\u0441\u043e\u043a \u0441 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u044f\u043c\u0438',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SlideReview',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField(verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xba\xd1\x81\xd1\x82')),
                ('person', models.CharField(max_length=40, verbose_name=b'\xd0\xa0\xd1\x83\xd0\xba\xd0\xbe\xd0\xb2\xd0\xbe\xd0\xb4\xd0\xb8\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c')),
                ('organization', models.CharField(max_length=50, verbose_name=b'\xd0\x9e\xd1\x80\xd0\xb3\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb7\xd0\xb0\xd1\x86\xd0\xb8\xd1\x8f')),
            ],
            options={
                'db_table': 'slider_review',
                'verbose_name': '\u0421\u043b\u0430\u0439\u0434',
                'verbose_name_plural': '\u0421\u043b\u0430\u0439\u0434\u0435\u0440 \u041e\u0442\u0437\u044b\u0432\u044b',
            },
            bases=(models.Model,),
        ),
    ]
