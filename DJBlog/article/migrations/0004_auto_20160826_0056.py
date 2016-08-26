# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20150610_0709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='password',
            field=models.CharField(null=True, blank=True, max_length=16),
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, to='article.Tag', related_name='posts'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='tag_name',
            field=models.CharField(max_length=64, primary_key=True, serialize=False),
        ),
    ]
