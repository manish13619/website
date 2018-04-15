from django.urls import path,include
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name='index'),  # index is the homepage of the section, name is optional
    path('login', views.login, name='login'),
    url(r'^genericviews/', include('genericviews.urls')),
]