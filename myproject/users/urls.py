from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path(
        route = 'register/', 
        view = views.register_view, 
        name = 'register'
    ),
]