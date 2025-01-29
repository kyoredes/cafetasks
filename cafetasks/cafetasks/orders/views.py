from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)
from cafetasks.orders.forms import OrdersCreateForm
from cafetasks.orders.models import Order
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin


class OrderListView(ListView):
    template_name = "table.html"
    model = Order
    paginate_by = 10
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
