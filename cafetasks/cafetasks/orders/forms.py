from django import forms
from cafetasks.orders.models import Order


class OrdersCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        labels = {
            "table_number": "Номер столика",
            "items": "Блюда",
            "executor": "Исполнитель",
            "status": "Статус",
        }
        fields = ["table_number", "items", "status", "executor"]
