from django.urls import path
from . import views

app_name = 'confession_app'

urlpatterns = [
    path('', views.listconfession, name='listconfession'),
    path('addconfession/', views.addconfession, name='addconfession'),
    path('signup/', views.SignUpView.as_view(), name="signup"),
    path('deleteconfession/<int:id>/', views.deleteconfession, name='deleteconfession'),
    path('log_out/', views.log_out, name='log_out'),
    path('terms/', views.terms, name='terms'),
    path('<int:confession_id>/like/', views.like_confession, name='like_confession'),
    path('<int:confession_id>/dislike/', views.dislike_confession, name='dislike_confession'),
]