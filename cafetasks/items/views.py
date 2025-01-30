from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from cafetasks.items.models import Item
from cafetasks.items.forms import ItemCreateForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin


class ItemListView(SuccessMessageMixin, ListView):
    model = Item
    template_name = "table.html"
    paginate_by = 10
    tables = ["ID", "Название", "Описание", "Цена", "Изменение"]
    context_object_name = "obj"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Меню"
        context["tables"] = self.tables
        context["list_name"] = "Items"
        context["url_name_update"] = "item_update"
        context["url_name_delete"] = "item_delete"
        context["url_name_create"] = "item_create"
        context["button_value_create"] = "Добавить в меню"

        return context


class ItemCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Item
    form_class = ItemCreateForm
    template_name = "form.html"
    success_url = reverse_lazy("item_list")
    success_message = "Объект меню создан"
    extra_context = {"title": "Добавление в меню", "button": "Добавить"}


class ItemUpdadeView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Item
    form_class = ItemCreateForm
    template_name = "form.html"
    success_url = reverse_lazy("item_list")
    success_message = "Объект меню успешно изменен"
    extra_context = {
        "title": "Изменение объекта меню",
        "button": "Изменить",
    }


class ItemDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Item
    template_name = "form.html"
    success_url = reverse_lazy("item_list")
    success_message = "Объект меню успешно удален"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Удаление объекта меню"
        context["button"] = "Да, удалить"
        context["value_to_delete"] = context["object"]
        return context
