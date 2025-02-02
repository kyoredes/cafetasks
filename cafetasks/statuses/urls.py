from django.urls import path
from cafetasks.statuses import views

urlpatterns = [
    path("", views.StatusListView.as_view(), name="status_list"),
    path("create/", views.StatusCreateView.as_view(), name="status_create"),
    path("update/<int:pk>/", views.StatusUpdadeView.as_view(), name="status_update"),
    path("delete/<int:pk>/", views.StatusDeleteView.as_view(), name="status_delete"),
]
