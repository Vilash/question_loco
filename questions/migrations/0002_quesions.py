# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quesions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('question', models.TextField()),
                ('order', models.IntegerField(default=0)),
                ('category', models.ForeignKey(to='questions.Category')),
            ],
        ),
    ]
