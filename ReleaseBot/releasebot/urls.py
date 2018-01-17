from django.conf.urls import url

from . import views

app_name = 'releasebot'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^release/(?P<release_id>[0-9]+)/$', views.release, name='release'),
]