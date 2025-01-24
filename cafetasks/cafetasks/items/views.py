from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from cafetasks.items.models import Item
from cafetasks.items.forms import ItemForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin


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
        context["url_name_change"] = "update_item"
        context["url_name_delete"] = "delete_item"
        context["button_value"] = "Добавить в меню"
        context["button_url"] = reverse_lazy("create_item")
        return context


class ItemCreateView(SuccessMessageMixin, CreateView):
    model = Item
    form_class = ItemForm
    template_name = "forms.html"
    success_url = reverse_lazy("items")
    success_message = "Объект меню создан"
    extra_context = {"title": "Добавление в меню", "button": "Добавить"}


class ItemUpdadeView(SuccessMessageMixin, UpdateView):
    model = Item
    form_class = ItemForm
    template_name = "forms.html"
    success_url = reverse_lazy("items")
    success_message = "Объект меню успешно изменен"
    extra_context = {
        "title": "Изменение объекта меню",
        "button": "Изменить",
    }


class ItemDeleteView(SuccessMessageMixin, DeleteView):
    model = Item
    template_name = "forms.html"
    success_url = reverse_lazy("items")
    success_message = "Объект меню успешно удален"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Удаление объекта меню"
        context["button"] = "Да, удалить"
        context["value_to_delete"] = context["object"]
        return context
