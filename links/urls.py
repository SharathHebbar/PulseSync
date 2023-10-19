from django.urls import path

from . import views

app_name = 'links'


urlpatterns = [
    path('', views.links, name='all_links'),
    path('<int:pk>/edit/', views.edit_links, name='edit_links'),
    path('<int:pk>/delete/', views.delete_links, name='delete_links'),
    path('create-links/', views.create_links, name='create_links'),
    path('categories/', views.categories, name='categories'),
    path('categories/<int:pk>/edit/', views.edit_category, name='edit_category'),
    path('categories/<int:pk>/delete/', views.delete_category, name='delete_category'),
    path('categories/create-category/', views.create_category, name='create_category'),

]
