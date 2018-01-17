from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^(?P<language>(ru|ua)?)', include('index.urls')),
    # url(r'^(?P<language>(ru|ua)?)/search', include('search.urls')),
    url(r'^(?P<language>(ru|ua)?)/news', include('news.urls')),
    # url(r'^(?P<language>(ru|ua)?)/about', include('about.urls')),
    # url(r'^(?P<language>(ru|ua)?)/tests', include('tests.urls')),
    url(r'^admin/', admin.site.urls)
]
