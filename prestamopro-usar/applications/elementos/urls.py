from django.contrib import admin
from django.urls import path, include
#from .views import ViewElements
from .views import ListOfelements, prestamo_form
from . import views
urlpatterns = [
    #path("inicio/", ViewElements.as_view(), name="inicio" ),
    path("list/", ListOfelements.as_view(), name="listaprestamo" ),
    path('index/', views.prestamo_form, name='ingreso_prestamo'),
]