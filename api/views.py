"""
Holds all our views
"""

from rest_framework import viewsets, permissions
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from rest_framework.exceptions import PermissionDenied

from .serializers import ItemSerializer, OrderSerializer
from .models import OrderItem, Order


class IsOwner(permissions.BasePermission):
    """
    Permission class that checks for model ownership
    """

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class ItemViewSet(viewsets.ModelViewSet):
    """
    Viewset that returns items
    """

    serializer_class = ItemSerializer
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)
    queryset = OrderItem.objects.all().order_by('name')


class OrderViewSet(viewsets.ModelViewSet):
    """
    Viewset that returns orders
    """

    serializer_class = OrderSerializer
    permission_classes = (IsOwner,)

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Order.objects.filter(owner=user)
        raise PermissionDenied()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
