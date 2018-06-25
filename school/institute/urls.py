from django.conf.urls import url
from . import views

app_name = 'blog'

urlpatterns = [
 # post views
 url(r'^$', views.register, name='register'),
]
