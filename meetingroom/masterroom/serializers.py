from .models import *
from rest_framework import serializers

class MasterRoom_Serializers(serializers.ModelSerializer):
    class Meta:
        model=MasterRoom
        fields='__all__'

class MasterRoom_Serializers_Input(serializers.Serializer):
    Rooms_name=serializers.CharField()



class Booking_Serializers(serializers.ModelSerializer):
    class Meta:
        model=Booking
        fields='__all__'

class BookingSearchSerializer(serializers.Serializer):
    room_id = serializers.CharField(required=False)
    start_time = serializers.TimeField(required=False)
    end_time = serializers.TimeField(required=False)
    date=serializers.DateField(required=False)