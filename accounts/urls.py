from django.urls import path 
from . import views
urlpatterns = [
    path('signup/', views.registerViewModel.as_view(), name='register'),
    path('signIn/', views.UserLoginView.as_view(), name='signIn'),
    path('signOut/', views.UserLogoutView.as_view(), name='signOut'),
    path('profile/', views.UserBankAccountUpdateView.as_view(), name='profile'),
]
