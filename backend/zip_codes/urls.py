from django.urls import path

from . import views

urlpatterns = [
    path('', views.zipCode_home),
    path('<str:zip_code_arg>/', views.zipCode_id)
]