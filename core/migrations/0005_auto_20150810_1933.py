# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_setup_seats'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='phone',
        ),
        migrations.AddField(
            model_name='ticket',
            name='email',
            field=models.EmailField(default='', max_length=256, verbose_name='Email'),
            preserve_default=False,
        ),
    ]
