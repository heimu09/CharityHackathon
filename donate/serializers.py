from rest_framework import serializers
from .models import Donation, BulletinBoard, Expense, CrowdFunding, CryptoDonation

class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = ("full_name", "phone_number", "telegram",
                   "amount", "currency", "stripe_token", "initiative", "donation_date")


class BulletinBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = BulletinBoard
        fields = ("full_name", "phone_number", "required_amount", 
                  "message", "created_at")


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ('id', 'amount', 'description', 
                  'comment', 'created_at')


class CrowdFundingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrowdFunding
        fields = '__all__'

class CryptoDonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CryptoDonation
        fields = ('id', 'account_number', 'address', 'amount', 'cryptocurrency', 'first_name', 'last_name')
