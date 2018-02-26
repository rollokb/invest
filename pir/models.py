from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import StreamField

from wagtail.core import blocks

from wagtailmarkdown.fields import MarkdownField
from wagtailmarkdown.blocks import MarkdownBlock
from wagtail.images.blocks import ImageChooserBlock

from wagtail.contrib.table_block.blocks import TableBlock

class HeadingBlock(blocks.StructBlock):
    level = blocks.ChoiceBlock(
        max_length = 2,
        choices = [
            ('h1', 'H1'),
            ('h2', 'H2'),
            ('h3', 'H3'),
            ('h4', 'H4'),
            ('h5', 'H5'),
            ('h6', 'H6'),
        ]
    )
    heading = blocks.CharBlock(max_length=250)

    class Meta:
        template = 'includes/heading.html'

class ContentWithFootnotesBlock(blocks.StructBlock):
    content = MarkdownBlock()
    footnotes = MarkdownBlock()

    class Meta:
        template = 'includes/content_with_footnotes.html'


class ImageLinkBlock(blocks.StructBlock):
    link = blocks.CharBlock()
    image = ImageChooserBlock(required=True)


class PirPage(Page):

    sections_choices = (
        ('0', 'Front Page'),
        ('1', 'Sector Overview'),
        ('2', 'Killer Facts'),
        ('3', 'Macro Context Between Countries'),
        ('4', 'UK Market Overview'),
        ('5', 'UK Business Info'),
        ('6', 'UK Geographic Overview'),
        ('7', 'Talent & Education'),
        ('8', 'Sector Initiatives'),
        ('9', 'R&D and Innovation'),
        ('10', 'R&D Innovation Case Study - Written'),
        ('11', 'Who\'s Here?'),
        ('12', 'Video Case Study'),
        ('13', 'Services offered by DIT'),
        ('14', 'Call to Action'),
        ('15', 'Testimonials'),
    )

    sectors_choices = (
        ('renewable-energy', 'Renewable Energy'),
        ('automotive', 'Automotive'),
        ('financial-services', 'Financial Services'),
        ('creative-services', 'Creative Services'),
        ('technology', 'Technology'),
        ('life-sciences', 'Life Sciences'),
    )

    markets_choices = (
        ('north-america', 'North America'),
        ('latin-america', 'Latin America'),
        ('europe', 'Europe'),
        ('turkey-caucasus', 'Turkey & Caucasus'),
        ('middle-east', 'Middle East'),
        ('africa', 'Africa'),
        ('south-asia', 'South Asia'),
        ('china', 'China'),
        ('asia-pacific', 'Asia Pacific'),
    )

    section = models.CharField(
        max_length = 64,
        choices = sections_choices,
    )

    sector = models.CharField(
        max_length = 32,
        choices = sectors_choices,
    )

    market = models.CharField(
        max_length = 32,
        choices = markets_choices,
    )

    body = StreamField([
        ('heading', HeadingBlock()),
        # ('hero_image', ImageChooserBlock(template="includes/hero_image.html")),
        ('hero_image', ImageChooserBlock()),
        ('content', MarkdownBlock()),
        ('content_with_footnotes', ContentWithFootnotesBlock()),
        ('footnotes', MarkdownBlock()),
        ('logo', ImageChooserBlock()),
        ('icon', ImageChooserBlock()),
        ('table', TableBlock()),
        ('video', blocks.CharBlock(max_length=256)),
        ('image_link', ImageLinkBlock()),
    ])
    
    content_panels = Page.content_panels + [
        FieldPanel('section'),
        FieldPanel('sector'),
        FieldPanel('market'),
        StreamFieldPanel('body'),
    ]

