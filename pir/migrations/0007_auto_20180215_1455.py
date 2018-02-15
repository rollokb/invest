# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-15 14:55
from __future__ import unicode_literals

from django.db import migrations
import wagtail.contrib.table_block.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks
import wagtailmarkdown.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('pir', '0006_pirpage_section'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pirpage',
            name='body',
            field=wagtail.core.fields.StreamField((('heading', wagtail.core.blocks.CharBlock(max_length=250)), ('hero_image', wagtail.images.blocks.ImageChooserBlock()), ('content', wagtailmarkdown.blocks.MarkdownBlock()), ('footnotes', wagtailmarkdown.blocks.MarkdownBlock()), ('logo', wagtail.images.blocks.ImageChooserBlock()), ('table', wagtail.contrib.table_block.blocks.TableBlock()))),
        ),
    ]
