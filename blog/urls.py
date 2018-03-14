from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^page/(?P<current_page>[1-9]+)', views.blog, name='blog'),
    url(r'^post/(?P<id>[1-9]+)', views.post, name='post'),
    url(r'^', views.blog, name='blog'),
]   