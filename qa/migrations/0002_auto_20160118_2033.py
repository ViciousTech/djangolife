# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anwsers',
            name='anwserer',
        ),
        migrations.RemoveField(
            model_name='questions',
            name='asker',
        ),
        migrations.AddField(
            model_name='anwsers',
            name='anwserer_email',
            field=models.EmailField(max_length=254, blank=True),
        ),
        migrations.AddField(
            model_name='questions',
            name='asker_email',
            field=models.EmailField(max_length=254, blank=True),
        ),
    ]
