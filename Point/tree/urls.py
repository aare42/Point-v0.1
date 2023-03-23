from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:leaf_id>/', views.leaf_detail, name='detail'),
]