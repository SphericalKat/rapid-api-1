"""
Holds all our model classes
"""

import uuid

import django
from django.db import models
from django.contrib.auth import get_user_model


class OrderItem(models.Model):
    """
    Represents an orderable item
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Order(models.Model):
    """
    Represents an order placed by a customer
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    status = models.CharField(max_length=10, default='p', choices=(
        ('p', 'pending'), ('c', 'complete')))
    expiry = models.DateTimeField(default=django.utils.timezone.now)

    def __str__(self):
        return str(f"{self.id} by {self.owner.get_username()}")
