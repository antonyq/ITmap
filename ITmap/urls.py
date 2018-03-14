from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', include('index.urls')),
    url(r'^search/', include('search.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^admin/', admin.site.urls)
]
