from django.urls import path
from . import views 


urlpatterns = [
    path('', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('user/', views.user_dashboard, name="user_home"),
    path('baseapp/admin/', views.admin_dashboard, name="admin_home"),
]