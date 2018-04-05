from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.models import Page

class PirFolderPage(Page):
    sections_choices = (
        (0, 'Front Page'),
        (1, 'Sector Overview'),
        (2, 'Killer Facts'),
        (3, 'Macro Context Between Countries'),
        (4, 'UK Market Overview'),
        (5, 'UK Business Info'),
        (6, 'UK Geographic Overview'),
        (7, 'Talent & Education'),
        (8, 'Sector Initiatives'),
        (9, 'R&D and Innovation'),
        (10, 'R&D Innovation Case Study - Written'),
        (11, 'Who\'s Here?'),
        (12, 'Video Case Study'),
        (13, 'Services offered by DIT'),
        (14, 'Call to Action'),
        (15, 'Testimonials'),
    )

    section = models.IntegerField(
        choices = sections_choices,
        blank = True,
        null = True
    )

    content_panels = Page.content_panels + [
        FieldPanel('section')
    ]