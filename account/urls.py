from django.urls import path
from . import views 

urlpatterns = [
    path('register', views.register, name= 'register'),
    #Login/Logout
    path('my-login',views.my_login, name= 'my-login'),
    path('dashboard',views.dashboard, name= 'dashboard'),
    path('logout',views.user_logout,name='logout'),
    path('profile-management',views.profile_management,name='profile-management'),
    path('delete-account',views.delete_account,name='delete-account'),
]
