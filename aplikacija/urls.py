from django.urls import path
from . import views

urlpatterns = [
    path("", views.trgovina, name="trgovina"),
    path("kosarica/", views.kosarica, name="kosarica"),
    path("update_item", views.updateItem, name="update_item"),
    path("hvala", views.thankYou, name="hvala"),
    path("vise/<pk>", views.vise, name="vise"),


]
