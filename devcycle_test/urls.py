from django.urls import path
from .views import home_page, admin_page, maintenance_page

urlpatterns = [
    path("", home_page, name="home"),
    path("admin", admin_page, name="admin"),
    path("maintenance", maintenance_page, name="maintenance")
]
