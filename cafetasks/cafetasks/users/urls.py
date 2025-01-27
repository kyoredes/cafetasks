from django.urls import path
from cafetasks.users import views

urlpatterns = [
    path("", views.UserListView.as_view(), name="user_list"),
    path("signup/", views.UserCreateView.as_view(), name="user_signup"),
    path("update/", views.UserUpdateView.as_view(), name="user_update"),
    path("delete/", views.UserDeleteView.as_view(), name="user_delete"),
]
