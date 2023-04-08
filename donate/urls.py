#urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('donations/', views.DonationViewSet.as_view({'get': 'list', 'post': 'create'}), name='donations-list-create'),
    path('donations/<int:pk>/', views.DonationViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='donations-detail'),
    path('financial_reports/', views.FinancialReportViewSet.as_view({'get': 'list'}), name='financial_reports-list'),
    path('bulletin_boards/', views.BulletinBoardViewSet.as_view({'get': 'list', 'post': 'create'}), name='bulletin_boards-list-create'),
    path('bulletin_boards/<int:pk>/', views.BulletinBoardViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='bulletin_boards-detail'),
    path('expenses/', views.ExpenseViewSet.as_view({'get': 'list', 'post': 'create'}), name='expense-list-create'),
    path('expenses/<int:pk>/', views.ExpenseViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='expense-retrieve-update-destroy'),
    path('projects/', views.CrowdFundingViewSet.as_view({'get': 'list', 'post': 'create'}), name='project-list-create'),
    path('projects/<int:pk>/', views.CrowdFundingViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='project-retrieve-update-destroy'),
    path('crypto_donations/', views.CryptoDonationViewSet.as_view({'get': 'list', 'post': 'create'}), name='crypto_donation-list-create'),
    path('crypto_donations/<int:pk>/', views.CryptoDonationViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='crypto_donation-retrieve-update-destroy'),

    path('stripe/donat/', views.PaymentView.as_view())
]
