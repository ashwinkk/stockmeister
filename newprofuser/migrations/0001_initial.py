# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('uname', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('password', models.CharField(max_length=50)),
                ('portfolios', models.CharField(max_length=1000)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
