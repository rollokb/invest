from django.conf.urls import include, url
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from django.contrib import admin
from django.conf import settings
import os.path

from wagtail.core import urls as wagtail_urls
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.search import urls as wagtailsearch_urls

# class boom():
#   a = 'b'

# urlpatterns = [
#     url(r'^report/', boom()),
# ]