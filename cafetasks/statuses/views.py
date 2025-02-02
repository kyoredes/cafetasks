from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)
from cafetasks.statuses.models import Status
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from cafetasks.statuses.forms import StatusCreateForm


class StatusListView(ListView):
    model = Status
    template_name = "table.html"
    context_object_name = "obj"
    tables = ["ID", "Название", "Создатель", "Дата создания", "Действие"]
    context_object_name = "obj"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Статусы"
        context["tables"] = self.tables
        context["list_name"] = "Statuses"
        context["url_name_update"] = "status_update"
        context["url_name_delete"] = "status_delete"
        context["url_name_create"] = "status_create"
        context["button_value_create"] = "Добавить статус"

        return context


class StatusCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Status
    form_class = StatusCreateForm
    template_name = "form.html"
    success_url = reverse_lazy("status_list")
    success_message = "Статус успешно создан"
    extra_context = {"title": "Создание статуса", "button": "Создать"}

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class StatusUpdadeView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Status
    form_class = StatusCreateForm
    template_name = "form.html"
    success_url = reverse_lazy("status_list")
    success_message = "Статус успешно изменен"
    extra_context = {
        "title": "Изменение статус",
        "button": "Изменить",
    }


class StatusDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Status
    template_name = "form.html"
    success_url = reverse_lazy("status_list")
    success_message = "Статус успешно удален"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Удаление статуса"
        context["button"] = "Да, удалить"
        context["value_to_delete"] = context["object"]
        return context
