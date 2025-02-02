from django.utils import timezone
from cafetasks.orders.models import Order, Status
from django.db.models import Sum

today = timezone.now().date()


start_of_day = timezone.make_aware(
    timezone.datetime.combine(today, timezone.datetime.min.time())
)
end_of_day = timezone.make_aware(
    timezone.datetime.combine(today, timezone.datetime.max.time())
)


def get_orders_count():
    return Order.objects.filter(
        status=Status.objects.filter(name="Оплачено").first(),
        created_at__gte=start_of_day,
        created_at__lt=end_of_day,
    ).count()


def get_daily_revenue():
    orders = Order.objects.filter(
        status=Status.objects.filter(name="Оплачено").first(),
        created_at__gte=start_of_day,
        created_at__lt=end_of_day,
    ).aggregate(total_cost_sum=Sum("items__cost"))

    total_sum = orders["total_cost_sum"] or 0
    return total_sum
