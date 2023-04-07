from rest_framework import serializers
from .models import Donation, BulletinBoard

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
