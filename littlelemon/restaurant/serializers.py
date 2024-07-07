from .models import *
from rest_framework import serializers

class MenuSerializer(serializers.ModelSerializer):
    class Meta():
        model = Menu
        fields = "__all__"

class BookingSerializer(serializers.ModelSerializer):
    class Meta():
        model = Booking
        fields = "__all__"

from rest_framework import serializers
from .models import MenuItem

class MenuItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = MenuItem
        fields = ['id','title','price','inventory']