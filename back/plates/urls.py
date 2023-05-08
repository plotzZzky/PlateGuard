from django.urls import path

from . import views


urlpatterns = [
    path('', views.show_all_plates, name='plates'),
    path('add/', views.create_plate, name='create_plate'),
    path('edit=<int:plate_id>/', views.edit_plate, name='edit_plate'),
    path('del=<int:plate_id>/', views.delete_plate, name='delete_plate'),
]