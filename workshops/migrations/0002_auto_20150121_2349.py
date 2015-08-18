# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='workshopregister',
            name='w_1',
            field=models.CharField(blank=True, max_length=30, choices=[(b'Bain&Company', b'Bain'), (b'Bank Zachodni WBK', b'bzwbk'), (b'PwC', b'pwc'), (b'Uber', b'uber')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='workshopregister',
            name='w_2',
            field=models.CharField(blank=True, max_length=30, choices=[(b'Bain&Company', b'Bain'), (b'Bank Zachodni WBK', b'bzwbk'), (b'PwC', b'pwc'), (b'Uber', b'uber')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='workshopregister',
            name='w_3',
            field=models.CharField(blank=True, max_length=30, choices=[(b'Bain&Company', b'Bain'), (b'Bank Zachodni WBK', b'bzwbk'), (b'PwC', b'pwc'), (b'Uber', b'uber')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='workshopregister',
            name='cv',
            field=models.FileField(upload_to=b'cv', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='workshopregister',
            name='graduation',
            field=models.IntegerField(choices=[(1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020)]),
            preserve_default=True,
        ),
    ]
