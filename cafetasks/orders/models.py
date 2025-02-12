from django.db import models
from cafetasks.items.models import Item
from django.contrib.auth import get_user_model
from django.db.models import Sum
from cafetasks.statuses.models import Status


class Order(models.Model):
    table_number = models.IntegerField()
    items = models.ManyToManyField(
        Item,
        related_name="orders",
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
    )
    executor = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def total_cost(self):
        values = self.items
        total = values.aggregate(total=Sum("cost"))
        return total["total"]

    def __str__(self):
        return f"заказ на столик {self.table_number}"
