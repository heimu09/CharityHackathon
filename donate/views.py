#views.py
import stripe
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
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



class PaymentView(APIView):
    def post(self, request):
        serializer = DonationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        amount = serializer.validated_data['amount']
        currency = serializer.validated_data['currency']
        description = serializer.validated_data['description']
        stripe_token = serializer.validated_data['stripe_token']
        date = serializer.validated_data['donation_date']

        stripe.api_key = "pk_test_51MuUcYIhJKBioU0zfwDGHgQZFcLFSnv1s7vZIZ20H0xpGUGLVRHypAHqQbybNgG3udcBemc5MtMaJwifLRdI33lK00zDCXOQyY"

        charge = stripe.Charge.create(
            amount=int(amount * 100),
            currency=currency,
            description=description,
            source=stripe_token
        )

        return Response({'status': 'success', 'charge_id': charge.id})