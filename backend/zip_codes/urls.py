from django.urls import path

from . import views

urlpatterns = [
    path('', views.zipCode_list_create_view),
    path('<int:pk>/', views.zipCode_detail_view)
]