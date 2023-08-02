from rest_framework import serializers
from .models import Cloths,Cart

class ClothSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cloths
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'