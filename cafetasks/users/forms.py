from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.forms import AuthenticationForm


class CustomUserCreateForm(UserCreationForm):
    usable_password = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Имя пользователя"
        self.fields["password1"].label = "Пароль"
        self.fields["password2"].label = "Подтверждение пароля"
        self.fields[
            "password1"
        ].help_text = """
        Пароль должен быть длиннее 8 символов и не состоять только из цифр
        """
        self.fields["username"].help_text = None
        self.fields["password2"].help_text = None


class CustomUserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Логин"
        self.fields["password"].label = "Пароль"
