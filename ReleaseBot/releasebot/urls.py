from django.conf.urls import url

from . import views

app_name = 'releasebot'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^release/(?P<release_id>[0-9]+)/$', views.release, name='release'),
    url(r'^account/(?P<account_id>[0-9]+)/(?P<environment_id>[0-9]+)/(?P<product_id>[0-9]+)/$', views.account, name='account'),
    url(r'^publish_release/$', views.publish_release, name='publish_release'),
    url(r'^success/$', views.success, name='success'),
]
