from django.urls import path
from . import views

urlpatterns = [
    path('', views.login,name='login'),
    path('signup/', views.signup,name='signup'),
    path('home/', views.home,name='home'),
    path('logout/', views.logout,name='logout'),
    path('adminlogin/', views.adminlogin,name='adminlogin'),
    path('adminpanel/', views.adminpanel,name='adminpanel'),
    path('adminlogout/', views.adminlogout,name='adminlogout'),
    path('delete/<int:id>', views.delete,name='delete'),
    path('edit/<int:id>', views.edit,name='edit'),
    path('update/<int:id>', views.update,name='update'),
    path('create/', views.create,name='create'),
]