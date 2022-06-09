# Generated by Django 2.1.8 on 2019-04-10 04:26

import coderedcms.blocks.base_blocks
import coderedcms.blocks.html_blocks
import coderedcms.fields
from django.db import migrations
import wagtail.contrib.table_block.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.embeds.blocks
import wagtail.images.blocks
import wagtail.snippets.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('coderedcms', '0012_merge_20190322_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carouselslide',
            name='content',
            field=coderedcms.fields.CoderedStreamField([], blank=True),
        ),
        migrations.AlterField(
            model_name='contentwall',
            name='content',
            field=coderedcms.fields.CoderedStreamField([], blank=True, verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='footer',
            name='content',
            field=coderedcms.fields.CoderedStreamField([], blank=True, verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='reusablecontent',
            name='content',
            field=coderedcms.fields.CoderedStreamField([], blank=True, verbose_name='content'),
        ),
    ]
