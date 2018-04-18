# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-11 13:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investment_report', '0002_auto_20180410_1614'),
    ]

    operations = [
        migrations.AddField(
            model_name='sectoroverview',
            name='footer_image_copy_attribution',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='sectoroverview',
            name='footer_image_copy_attribution_ar',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sectoroverview',
            name='footer_image_copy_attribution_de',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sectoroverview',
            name='footer_image_copy_attribution_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sectoroverview',
            name='footer_image_copy_attribution_es',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sectoroverview',
            name='footer_image_copy_attribution_fr',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sectoroverview',
            name='footer_image_copy_attribution_ja',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sectoroverview',
            name='footer_image_copy_attribution_pt',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sectoroverview',
            name='footer_image_copy_attribution_zh_cn',
            field=models.TextField(blank=True, null=True),
        ),
    ]