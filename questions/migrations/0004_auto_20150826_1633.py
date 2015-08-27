# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_auto_20150826_1632'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Questions',
            new_name='Question',
        ),
    ]
