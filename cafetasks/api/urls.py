from rest_framework import routers
from cafetasks.api import views
from django.urls import include, path
from djoser.views import UserViewSet

router = routers.DefaultRouter()
router.register("statuses", views.StatusAPIViewSet, basename="statuses_api")
router.register("items", views.ItemAPIViewSet, basename="items_api")
router.register("orders", views.OrderAPIViewSet, basename="orders_api")
router.register("users", UserViewSet, basename="users_api")


urlpatterns = [path("", include(router.urls))]
