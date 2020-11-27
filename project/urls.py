from django.urls import path
from project import views

from .views import Djangov2, DjangoRestFramework

urlpatterns = [
    path('aboutme', views.aboutme, name='aboutme'),
    path('datascience', views.datascience, name='datascience'),
    path('django', views.django, name='django'),
    path('djangov2', Djangov2.as_view(), name='djangov2'),
    path('apis-drf', DjangoRestFramework.as_view(), name='drf'),
    path('', views.index, name='index'),
]