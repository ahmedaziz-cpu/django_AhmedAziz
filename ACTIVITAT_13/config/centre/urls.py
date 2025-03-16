from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('professors/', views.professors, name='professors'),
    path('alumnes/', views.alumnes, name='alumnes'),
    path('books/book/<str:bk>/', views.book, name='book'),
    path('books/', views.books, name='books'),
    path('alumne_form/', views.user_form, name='form'),
    path('professor_form/', views.users_form, name='form1'),
    path('alumnes/<int:pk>/', views.alumnes_detalles, name='alumnes_detalles'),
    path('professors/<int:pk>/', views.professors_detalles, name='professors_detalles'),

    ##path('',views.)


]