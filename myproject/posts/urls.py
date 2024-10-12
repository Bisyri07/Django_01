from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path(route='', view=views.posts_list, name='list'),
    path(route='<slug:slug>', view=views.post_page, name='page'),
]