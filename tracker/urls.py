from django.contrib.auth import views as auth_views
from django.urls import path
from .views import register, dashboard, add_investment, landing_page, list_investments, edit_investment, delete_investment

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('register/', register, name='register'),
    path('dashboard/', dashboard, name='dashboard'),
    path('add/', add_investment, name='add_investment'),
    path('investments/', list_investments, name='list_investments'),
    path('login/', auth_views.LoginView.as_view(template_name='tracker/login.html'), name='login'),
    path('investments/edit/<int:id>/', edit_investment, name='edit_investment'),
    path('investments/delete/<int:id>/', delete_investment, name='delete_investment'),
    path('logout/', auth_views.LogoutView.as_view(next_page='landing_page'), name='logout'),
]