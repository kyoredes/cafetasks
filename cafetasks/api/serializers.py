from cafetasks.statuses.models import Status
from django.contrib.auth import get_user_model
from cafetasks.items.models import Item
from cafetasks.orders.models import Order
from rest_framework.serializers import ModelSerializer
from djoser.serializers import UserCreateSerializer


class StatusSerializer(ModelSerializer):
    class Meta:
        model = Status
        fields = ["name", "created_at", "user"]


class UserSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id", "username"]


class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = get_user_model()
        fields = ["username", "password"]


class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = ["name", "description", "cost"]


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ["table_number", "status__name", "executor"]
