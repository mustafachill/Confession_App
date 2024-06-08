from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'confession_app'

urlpatterns = [
    path('', views.listconfession, name='listconfession'),
    path('addconfession/', views.addconfession, name='addconfession'),
    path('addconfessionbyform/', views.addconfessionbyform, name='addconfessionbyform'),
    path('addconfessionbymodelform/', views.addconfessionbymodelform, name='addconfessionbymodelform'),
    path('signup/',views.SignUpView.as_view(),name="signup"),
    path('deleteconfession/<int:id>', views.deleteconfession, name='deleteconfession'),
    path('log_out/', views.log_out, name='log_out'),
    path('terms/', views.terms, name='terms'),
]
