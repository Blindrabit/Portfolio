from django.urls import path
from project import views

urlpatterns = [
    path('aboutme', views.aboutme, name='aboutme'),
    path('datascience', views.datascience, name='datascience'),
    path('django', views.django, name='django'),
    path('', views.index, name='index')
]