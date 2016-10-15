# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datamine', '0003_auto_20160105_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stocks_intraday',
            name='ChangeinPercent',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
    ]
