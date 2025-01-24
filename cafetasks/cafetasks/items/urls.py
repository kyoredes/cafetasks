from django.urls import path
from cafetasks.items import views

urlpatterns = [
    path("", views.ItemListView.as_view(), name="items"),
    path("create/", views.ItemCreateView.as_view(), name="create_item"),
    path("update/<int:pk>/", views.ItemUpdadeView.as_view(), name="update_item"),
    path("delelte/<int:pk>/", views.ItemDeleteView.as_view(), name="delete_item"),
]
