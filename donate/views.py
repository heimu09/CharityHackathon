from rest_framework import viewsets, generics
from django_filters import rest_framework as filters
from rest_framework.filters import OrderingFilter
from .models import Donation, BulletinBoard
from .serializers import DonationSerializer, BulletinBoardSerializer



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