from django.urls import path
from cafetasks.orders import views

urlpatterns = [
    path("", views.OrderListView.as_view(), name="order_list"),
    path("<int:pk>/", views.OrderDetailView.as_view(), name="order_detail"),
    path("create/", views.OrderCreateView.as_view(), name="order_create"),
    path("update/<int:pk>/", views.OrderUpdadeView.as_view(), name="order_update"),
    path("delete/<int:pk>/", views.OrderDeleteView.as_view(), name="order_delete"),
    path("revenue/", views.OrderRevenueView.as_view(), name="revenue"),
]
