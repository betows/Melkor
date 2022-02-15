from django.urls import path, include
from .views import dashboard, home, profile_list, profile, user_login
from . import views

app_name = "dwitter"

urlpatterns = [
    path("", home, name="home"),
    path("profile_list/", profile_list, name="profile_list"),
    path("profile/<int:pk>", profile, name="profile"),
    path("register", views.register_request, name="register"),
    path("dashboard/", dashboard, name="dashboard"),
    path('accounts/', include('django.contrib.auth.urls')),
]
