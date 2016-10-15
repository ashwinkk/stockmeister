# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datamine', '0002_auto_20160105_1417'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stocks_intraday',
            name='PercentChange',
        ),
        migrations.AddField(
            model_name='stocks_intraday',
            name='ChangeinPercent',
            field=models.CharField(default=b'NULL', max_length=20, null=True, blank=True),
        ),
    ]
