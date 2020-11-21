"""
Place to register models in the admin site
"""

from django.contrib import admin
from .models import OrderItem, Order


admin.site.register(OrderItem)
admin.site.register(Order)
