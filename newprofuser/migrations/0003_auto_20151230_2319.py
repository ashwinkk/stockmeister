# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newprofuser', '0002_auto_20151230_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='emailid',
            field=models.EmailField(max_length=40),
        ),
    ]
