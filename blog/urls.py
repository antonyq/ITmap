from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^page/(?P<current_page>[0-9]+)', views.blog, name='blog'),
    url(r'^', views.blog, name='blog'),
    url(r'^post/(?P<id>[0-9]+)', views.post, name='post'),
]   