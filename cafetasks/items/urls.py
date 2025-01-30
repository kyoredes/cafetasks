from django.urls import path
from cafetasks.items import views

urlpatterns = [
    path("", views.ItemListView.as_view(), name="item_list"),
    path("create/", views.ItemCreateView.as_view(), name="item_create"),
    path("update/<int:pk>/", views.ItemUpdadeView.as_view(), name="item_update"),
    path("delete/<int:pk>/", views.ItemDeleteView.as_view(), name="item_delete"),
]
