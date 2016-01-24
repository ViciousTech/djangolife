# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='anwsers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.TextField(max_length=300)),
                ('anwserer_email', models.EmailField(max_length=254, blank=True)),
                ('anwser', models.TextField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='questions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.TextField(max_length=300)),
                ('asker_email', models.EmailField(max_length=254, blank=True)),
                ('description', models.TextField(max_length=1000)),
            ],
        ),
    ]
