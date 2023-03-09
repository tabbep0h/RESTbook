from django.urls import path
from . import views

urlpatterns = [
    path("books", views.bookList),
    path("books-detail/<int:pk>", views.bookDetail),
    path("book-create", views.bookCreate),
    path("book-update/<int:pk>", views.bookUpdate),
    path("book-delete/<int:pk>", views.bookDelete),
]
