from rest_framework import viewsets, permissions
from rest_framework.exceptions import PermissionDenied

from .serializers import ItemSerializer, OrderSerializer
from .models import OrderItem, Order


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user

class ItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all().order_by('name')
    serializer_class = ItemSerializer

    

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = (IsOwner,)
    
    # Ensure a user sees only own Note objects.
    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Order.objects.filter(owner=user)
        raise PermissionDenied()
    
    # Set user as owner of a Notes object.
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)