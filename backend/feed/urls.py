
from django.contrib.auth.views import LogoutView
from django.urls import path, include

from . import views

urlpatterns = [
	path('', views.home, name='home'),
    path('logout/', LogoutView.as_view(), name='logout'),
]