from django.urls import path

from . import views


urlpatterns = [
    path('login/', views.login),
    path('register/', views.register_user),
    path('offices/', views.get_offices),
]
