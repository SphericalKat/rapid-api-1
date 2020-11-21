"""
Holds all our url routes
"""

from django.urls import include, path
from rest_framework import routers


from . import views


router = routers.DefaultRouter()
router.register(r'orders', views.OrderViewSet, basename='Order')
router.register(r'items', views.ItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
