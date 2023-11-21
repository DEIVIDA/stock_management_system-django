"""
URL configuration for stock_management_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from stock_management import views
from django.urls import include
from stock_management.views import add_category, category_list


urlpatterns = [
    path("", views.home, name="home"),
    path("admin/", admin.site.urls),
    path("list_item/", views.list_item, name="list_items"),
    path("update_items/<str:pk>/", views.update_items, name="update_items"),
    path("delete_items/<str:pk>/", views.delete_items, name="delete_items"),
    path("add_item/", views.add_item, name="add_item"),
    path("stock_detail/<str:pk>/", views.stock_detail, name="stock_detail"),
    path("issue_items/<str:pk>/", views.issue_items, name="issue_items"),
    path("receive_items/<str:pk>/", views.receive_items, name="receive_items"),
    path("reorder_level/<str:pk>/", views.reorder_level, name="reorder_level"),
    path("accounts/", include("registration.backends.default.urls")),
    path("list_history/", views.list_history, name="list_history"),
    path("add_category/", add_category, name="add_category"),
    path("category_list/", category_list, name="category_list"),
]
