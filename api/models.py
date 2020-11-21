import uuid
from datetime import datetime

import django
from django.db import models
from django.contrib.auth.models import User


class OrderItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    price = models.IntegerField()

    def __str__(self):
        return self.name

class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    status = models.CharField(max_length=10, default='p', choices=(('p', 'pending'), ('c', 'complete')))
    expiry = models.DateTimeField(default=django.utils.timezone.now)

    def __str__(self):
        return str(self.owner.get_username())
