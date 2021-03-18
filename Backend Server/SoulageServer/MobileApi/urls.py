from django.urls import path, include
from . import views
from NeuralNetwork.views import get_dashboard_data

urlpatterns = [
    path("login", views.LoginView.as_view(), name="login"),
    path("get_dashboard_data", get_dashboard_data, name="get_dashboard_data"),
]