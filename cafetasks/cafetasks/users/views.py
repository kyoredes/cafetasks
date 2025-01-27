from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from cafetasks.users.forms import CustomUserLoginForm, CustomUserCreateForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy


class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = "forms.html"
    form_class = CustomUserLoginForm
    success_message = "Вы залогинены"
    extra_context = {"title": "Вход", "button": "Войти"}


class UserLogoutView(SuccessMessageMixin, LogoutView):
    success_message = "Вы вышли из системы"


class UserListView(SuccessMessageMixin, ListView):
    model = get_user_model()
    paginate_by = 10
    template_name = "table.html"


class UserCreateView(SuccessMessageMixin, CreateView):
    model = get_user_model()
    form_class = CustomUserCreateForm
    success_message = "Вы зарегистрированы"
    success_url = reverse_lazy("index")
    template_name = "forms.html"
    extra_context = {"title": "Регистрация", "button": "Зарегистрироваться"}


class UserUpdateView(SuccessMessageMixin, UpdateView):
    model = get_user_model()
    form_class = CustomUserCreateForm
    success_url = reverse_lazy("index")
    success_message = "Данные успешно обновлены"
    template_name = "forms.html"
    extra_context = {"title": "Изменение информации", "button": "Изменить"}


class UserDeleteView(SuccessMessageMixin, DeleteView):
    model = get_user_model()
    success_messsage = "Вы удалили свой аккаунт"
    success_url = reverse_lazy("index")
    template_name = "forms.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Удаление аккаунта"
        context["button"] = "Да, удалить"
        context["name"] = "аккаунт"
        context["value_to_delete"] = context["object"]
        return context
