# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import workshops.models


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0002_auto_20150121_2349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workshopregister',
            name='cv',
            field=models.FileField(upload_to=workshops.models.file_name, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='workshopregister',
            name='w_1',
            field=models.CharField(max_length=30, choices=[(b'bain', b'Bain&Company'), (b'bzwbk', b'Bank Zachodni WBK'), (b'pwc', b'PwC'), (b'uber', b'Uber')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='workshopregister',
            name='w_2',
            field=models.CharField(max_length=30, choices=[(b'bain', b'Bain&Company'), (b'bzwbk', b'Bank Zachodni WBK'), (b'pwc', b'PwC'), (b'uber', b'Uber')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='workshopregister',
            name='w_3',
            field=models.CharField(blank=True, max_length=30, choices=[(b'bain', b'Bain&Company'), (b'bzwbk', b'Bank Zachodni WBK'), (b'pwc', b'PwC'), (b'uber', b'Uber')]),
            preserve_default=True,
        ),
    ]
