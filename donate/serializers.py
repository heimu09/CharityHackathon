from rest_framework import serializers
from .models import BulletinBoard


class BulletinBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = BulletinBoard
        fields = ('name', 'phone_number', 'telegram', 'position', 'message',)