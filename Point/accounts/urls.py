from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('register/', views.register, name='register'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
 #   path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
]