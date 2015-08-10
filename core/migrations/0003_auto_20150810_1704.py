# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20150810_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='phone',
            field=models.CharField(max_length=256, verbose_name='\u0442\u0435\u043b\u0435\u0444\u043e\u043d'),
        ),
    ]
