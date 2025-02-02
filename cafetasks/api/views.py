from rest_framework.viewsets import ModelViewSet
from cafetasks.statuses.models import Status
from django.contrib.auth import get_user_model
from cafetasks.items.models import Item
from cafetasks.orders.models import Order
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from cafetasks.api import serializers


class StatusAPIViewSet(ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = serializers.StatusSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class UserAPIViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = serializers.UserSerializer


class ItemAPIViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = serializers.ItemSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class OrderAPIViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = serializers.OrderSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
