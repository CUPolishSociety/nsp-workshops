# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WorkshopRegister',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('surname', models.CharField(max_length=250)),
                ('email', models.EmailField(unique=True, max_length=75)),
                ('uni', models.CharField(max_length=200)),
                ('graduation', models.IntegerField()),
                ('cv', models.FileField(upload_to=b'cv')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
