from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^$',views.post_line,name ='post_line'),
]