# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('cate_name', models.CharField(serialize=False, max_length=100, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('password', models.CharField(null=True, max_length=16)),
                ('author', models.ForeignKey(related_name='posts', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(related_name='posts', to='article.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('tag_name', models.CharField(serialize=False, max_length=50, primary_key=True)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(related_name='posts', to='article.Tag'),
        ),
    ]
