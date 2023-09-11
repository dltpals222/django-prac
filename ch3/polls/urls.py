from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("userInfo/", views.userManagement, name="userManagement"),
    path("create/", views.create, name="create"),
    path("update/", views.update, name="update"),
    path("delete/", views.delete, name="delete"),
]
