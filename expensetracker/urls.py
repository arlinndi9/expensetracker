
from django.urls import path, include
from expensetracker import views

urlpatterns = [
    path('',views.home,name='home'),
    path('delete_expense/<int:id>',views.deleteexpensive,name='delete_expense'),
    path('update_expense/<int:id>',views.updateexpensive,name='update_expense'),
]