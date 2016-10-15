# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newprofuser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='emailid',
            field=models.EmailField(default=None, max_length=40),
        ),
        migrations.AlterField(
            model_name='user',
            name='portfolios',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
    ]
