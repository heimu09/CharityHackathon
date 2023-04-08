#views.py
from rest_framework import viewsets
from django_filters import rest_framework as filters
from rest_framework.filters import OrderingFilter
from .models import Donation, BulletinBoard, Expense, CrowdFunding, CryptoDonation
from .serializers import DonationSerializer, BulletinBoardSerializer, ExpenseSerializer, CrowdFundingSerializer, CryptoDonationSerializer


class DonationViewSet(viewsets.ModelViewSet):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer


class BulletinBoardViewSet(viewsets.ModelViewSet):
    queryset = BulletinBoard.objects.all()
    serializer_class = BulletinBoardSerializer


class DonationFilter(filters.FilterSet):
    initiative = filters.CharFilter(field_name="initiative")
    full_name = filters.CharFilter(field_name="full_name", lookup_expr="icontains")

    class Meta:
        model = Donation
        fields = ['initiative', 'full_name']


class FinancialReportViewSet(viewsets.ModelViewSet):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer
    filter_backends = (OrderingFilter, filters.DjangoFilterBackend)
    filterset_class = DonationFilter
    ordering_fields = ['amount']


class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    filter_backends = (OrderingFilter,)
    ordering_fields = ['amount']

class CrowdFundingViewSet(viewsets.ModelViewSet):
    queryset = CrowdFunding.objects.all()
    serializer_class = CrowdFundingSerializer

class CryptoDonationViewSet(viewsets.ModelViewSet):
    queryset = CryptoDonation.objects.all()
    serializer_class = CryptoDonationSerializer
