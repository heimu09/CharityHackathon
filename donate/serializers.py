from rest_framework import serializers
from .models import Donation

class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = ("full_name", "phone_number", "telegram",
                   "amount", "initiative", "donation_date")
