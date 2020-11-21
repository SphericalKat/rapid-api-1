"""
Holds all our serializers
"""
from rest_framework import serializers

from .models import OrderItem, Order


class ItemSerializer(serializers.ModelSerializer):
    """
    Serializes Item models
    """
    class Meta:
        model = OrderItem
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    """
    Serializes Order models
    """
    class Meta:
        model = Order
        exclude = ["owner"]
