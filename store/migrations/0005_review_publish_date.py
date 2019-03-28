# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20190328_1122'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='publish_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
