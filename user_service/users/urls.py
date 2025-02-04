from django.urls import path
from .views import RegisterUserView, LoginView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]
