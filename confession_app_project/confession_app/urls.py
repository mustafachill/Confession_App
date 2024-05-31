from django.urls import path
from . import views

app_name = 'confession_app'

urlpatterns = [
    path('', views.listconfesion),
    path('addconfession/', views.addconfesion),
]
