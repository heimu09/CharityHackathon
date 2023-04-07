from django.urls import path
from . import views

urlpatterns = [
    path('donations/', views.DonationViewSet.as_view({'get': 'list', 'post': 'create'}), name='donations-list-create'),
    path('donations/<int:pk>/', views.DonationViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='donations-detail'),
    path('financial_reports/', views.FinancialReportViewSet.as_view({'get': 'list'}), name='financial_reports-list'),
    path('bulletin_boards/', views.BulletinBoardViewSet.as_view({'get': 'list', 'post': 'create'}), name='bulletin_boards-list-create'),
    path('bulletin_boards/<int:pk>/', views.BulletinBoardViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='bulletin_boards-detail'),
]
