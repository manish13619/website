from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^genericviews/', include('genericviews.urls')),
    url(r'^homepage/',include('homepage.urls')),
]