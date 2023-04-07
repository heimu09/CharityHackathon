from django.urls import path
from . import views

urlpatterns = [
    path('donations/', views.DonationViewSet.as_view({'get': 'list', 'post': 'create'}), name='donations-list-create'),
    path('donations/<int:pk>/', views.DonationViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='donations-detail'),
]
