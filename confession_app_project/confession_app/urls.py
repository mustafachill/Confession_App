from django.urls import path
from . import views

app_name = 'confession_app'

urlpatterns = [
    path('', views.listconfession, name='listconfession'),
    path('addconfession/', views.addconfession, name='addconfession'),
]
