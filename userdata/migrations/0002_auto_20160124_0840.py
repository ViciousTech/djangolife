# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=254)),
                ('username', models.CharField(max_length=30)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('dob', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='userdata',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_joied', models.DateField()),
                ('last_active', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='anwsers',
        ),
        migrations.DeleteModel(
            name='questions',
        ),
        migrations.AddField(
            model_name='user',
            name='info',
            field=models.ForeignKey(to='userdata.userdata'),
        ),
    ]
