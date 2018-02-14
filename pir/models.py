from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import StreamField

from wagtail.core import blocks

from wagtailmarkdown.fields import MarkdownField
from wagtailmarkdown.blocks import MarkdownBlock
from wagtail.images.blocks import ImageChooserBlock


class PirPage(Page):

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

    sector = models.CharField(
        max_length = 32,
        choices = sectors_choices,
    )

    market = models.CharField(
        max_length = 32,
        choices = markets_choices,
    )

    body = StreamField([
        ('heading', blocks.CharBlock(max_length=250)),
        ('hero_image', ImageChooserBlock()),
        ('content', MarkdownBlock()),
        ('footnotes', MarkdownBlock()),
        ('logo', ImageChooserBlock()),
    ])
    
    content_panels = Page.content_panels + [
        FieldPanel('sector'),
        FieldPanel('market'),
        StreamFieldPanel('body'),
    ]

