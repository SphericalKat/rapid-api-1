from rest_framework import serializers

from .models import OrderItem, Order


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = ['owner']