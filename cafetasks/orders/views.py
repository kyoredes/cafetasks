from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
    TemplateView,
)
from cafetasks.orders.forms import OrdersCreateForm
from cafetasks.orders.models import Order
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from cafetasks.utils.calculate_data import get_orders_count, get_daily_revenue
from cafetasks.orders.documents import OrderDocument
from django.shortcuts import render


class SearchResultsList(ListView):
    def get(self, request, *args, **kwargs):
        query = request.GET.get("q")
        if query:
            if query.isdigit():
                search = (
                    OrderDocument().search().query("match", table_number=int(query))
                )
            else:
                search = (
                    OrderDocument()
                    .search()
                    .query(
                        "nested", path="status", query={"match": {"status.name": query}}
                    )
                )

            results = search.execute()
            orders_result = [
                {"id": hit.id, "table_number": hit.table_number, "status": hit.status}
                for hit in results
            ]
            return render(request, "search.html", context={"results": orders_result})
        return render(request, "search.html")


class OrderRevenueView(TemplateView):
    template_name = "revenue.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Выручка за смену"
        context["orders_count"] = get_orders_count()
        context["revenue"] = get_daily_revenue()

        return context


class OrderListView(ListView):
    template_name = "table.html"
    model = Order
    tables = [
        "ID",
        "Номер стола",
        "Заказанное",
        "Цена",
        "Исполнитель",
        "Статус",
        "Действие",
    ]
    context_object_name = "obj"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Заказы"
        context["tables"] = self.tables
        context["list_name"] = "Orders"
        context["url_name_update"] = "order_update"
        context["url_name_delete"] = "order_delete"
        context["url_name_detail"] = "order_detail"
        context["url_name_create"] = "order_create"
        context["button_value_create"] = "Добавить заказ"

        return context


class OrderDetailView(LoginRequiredMixin, DetailView):
    template_name = "detail.html"
    model = Order
    context_object_name = "obj"
    tables = ["ID", "Номер стола", "Заказанное", "Цена заказа", "Статус", "Исполнитель"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Заказ"
        context["tables"] = self.tables
        context["list_name"] = "Orders"
        context["url_name_update"] = "order_update"
        context["url_name_delete"] = "order_delete"
        return context


class OrderCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Order
    form_class = OrdersCreateForm
    template_name = "form.html"
    success_url = reverse_lazy("order_list")
    success_message = "Заказ успешно создан"
    extra_context = {"title": "Добавление заказа", "button": "Добавить"}


class OrderUpdadeView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Order
    form_class = OrdersCreateForm
    template_name = "form.html"
    success_url = reverse_lazy("order_list")
    success_message = "Заказ успешно изменен"
    extra_context = {
        "title": "Изменение заказа",
        "button": "Изменить",
    }


class OrderDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Order
    template_name = "form.html"
    success_url = reverse_lazy("order_list")
    success_message = "Заказ успешно удален"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Удаление заказа"
        context["button"] = "Да, удалить"
        context["value_to_delete"] = context["object"]
        return context
