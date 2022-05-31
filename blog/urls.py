from django.urls import path
from . import views

urlpatterns = [
    path('', views.article, name='article'),
    path('article/', views.article, name='article_write'),
    path('article/<int:id>', views.article_list, name='article_categoty_list'),
    path('category/', views.catecory, name='category_list'),
]