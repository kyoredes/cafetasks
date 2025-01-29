from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from cafetasks.users.forms import CustomUserLoginForm, CustomUserCreateForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.contrib import messages


class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = "form.html"
    form_class = CustomUserLoginForm
    success_message = "Вы залогинены"
    extra_context = {"title": "Вход", "button": "Войти"}


class UserLogoutView(SuccessMessageMixin, LogoutView):
    success_message = "Вы вышли из системы"


class UserCreateView(SuccessMessageMixin, CreateView):
    model = get_user_model()
    form_class = CustomUserCreateForm
    success_message = "Вы зарегистрированы"
    success_url = reverse_lazy("index")
    template_name = "form.html"
    extra_context = {"title": "Регистрация", "button": "Зарегистрироваться"}


class UserUpdateView(
    SuccessMessageMixin, LoginRequiredMixin, UserPassesTestMixin, UpdateView
):
    model = get_user_model()
    form_class = CustomUserCreateForm
    success_url = reverse_lazy("index")
    success_message = "Данные успешно обновлены"
    template_name = "form.html"
    extra_context = {"title": "Изменение информации", "button": "Изменить"}

    def test_func(self):
        return self.request.user.id == self.kwargs.get("pk")

    def handle_no_permission(self):
        text_error = "У вас нет разрешения для редактирования данных этого пользователя"
        messages.error(self.request, text_error)
        return super().handle_no_permission()


class UserDeleteView(
    SuccessMessageMixin, LoginRequiredMixin, UserPassesTestMixin, DeleteView
):
    model = get_user_model()
    success_messsage = "Вы удалили свой аккаунт"
    success_url = reverse_lazy("index")
    template_name = "form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Удаление аккаунта"
        context["button"] = "Да, удалить"
        context["name"] = "аккаунт"
        context["value_to_delete"] = context["object"]
        return context

    def test_func(self):
        return self.request.user.id == self.kwargs.get("pk")
