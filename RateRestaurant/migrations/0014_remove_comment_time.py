# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RateRestaurant', '0013_comment_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='time',
        ),
    ]
