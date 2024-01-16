from django.urls import path
from . import views
urlpatterns = [
    path("register/", views.UserRegistrationView.as_view(), name='register'),
    path("login/", views.UserLoginView.as_view(), name='login'),
    path("logout/", views.UserLogoutView.as_view(), name='logout'),
    path("profile/", views.UserProfileView, name='profile'),
    path('edit/<int:id>/', views.edit_profile.as_view() , name='edit_profile'),
    path('password_change/', views.passChange, name='password_change'),
    path('active/<uid64>/<token>/', views.activate, name = 'activate'),
    path('deposite/', views.deposite_money, name='deposite'),
    # path('deposite/', views.DepositeMoney.as_view(), name="deposite")
]
