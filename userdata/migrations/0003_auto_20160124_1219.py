# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0002_auto_20160124_0840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='date_joied',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='last_active',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
