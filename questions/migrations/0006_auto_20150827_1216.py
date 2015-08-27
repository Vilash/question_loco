# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0005_auto_20150826_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='category',
            field=models.CharField(max_length=255),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
