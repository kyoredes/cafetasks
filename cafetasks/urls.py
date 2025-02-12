"""
URL configuration for cafetasks project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from cafetasks.users.views import UserLoginView
from django.contrib.auth.views import LogoutView
from cafetasks.views import index

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("items/", include("cafetasks.items.urls")),
    path("users/", include("cafetasks.users.urls")),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("orders/", include("cafetasks.orders.urls")),
    path("statuses/", include("cafetasks.statuses.urls")),
    path("api/", include("cafetasks.api.urls")),
]
