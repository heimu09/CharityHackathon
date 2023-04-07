from rest_framework import serializers
from .models import Donation, BulletinBoard, Expense, CrowdFunding

class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = ("full_name", "phone_number", "telegram",
                   "amount", "initiative", "donation_date")


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
