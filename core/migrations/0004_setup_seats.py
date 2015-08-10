# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20150810_1704'),
    ]

    operations = [
        migrations.AddField(
            model_name='setup',
            name='seats',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043c\u0435\u0441\u0442', blank=True),
            preserve_default=True,
        ),
    ]
