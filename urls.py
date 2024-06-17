from django.urls import path

from . import views


urlpatterns = [
    # ex: /polls/
    path("", views.main, name="main"),
    path("author/", views.index, name="index"),
    path("book/", views.book, name="book"),
    path("publisher/", views.publisher, name="publisher"),
    path('succes', views.succes, name='succes')

]