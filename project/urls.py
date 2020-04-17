from django.urls import path
from project import views

urlpatterns = [
    path('aboutme', views.aboutme, name='aboutme')
]