from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    path('register/', views.register_view, name='register'),

    path('login/', views.login_view, name='login'),

    path('logout/', views.logout_view, name='logout'),

    path('expenses/', views.expense_list, name='expense_list'),

    path('add/', views.add_expense, name='add_expense'),

    path('update/<int:expense_id>', views.update_expense, name = "update_expense"),

    path('delete/<int:expense_id>', views.delete_expense, name = "delete_expense"),

]