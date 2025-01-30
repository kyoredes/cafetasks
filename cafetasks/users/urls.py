from django.urls import path
from cafetasks.users import views

urlpatterns = [
    path("signup/", views.UserCreateView.as_view(), name="user_signup"),
    path("update/<int:pk>/", views.UserUpdateView.as_view(), name="user_update"),
    path("delete/<int:pk>/", views.UserDeleteView.as_view(), name="user_delete"),
]
