# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('header', '0002_auto_20150407_1931'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': '\u041a\u043e\u043d\u0442\u0430\u043a\u0442\u044b', 'verbose_name_plural': '\u041a\u043e\u043d\u0442\u0430\u043a\u0442\u044b'},
        ),
        migrations.AlterModelOptions(
            name='logo',
            options={'verbose_name': '\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0441\u0430\u0439\u0442\u0430', 'verbose_name_plural': '\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0441\u0430\u0439\u0442\u0430'},
        ),
    ]
