from django.urls import path
from .views import index

urlpatterns = [
    path('', index),
    path('Login', index),
    path('Signup', index),
    path('UserDash', index),
    path('WritePost', index)
]
