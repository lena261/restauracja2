from django.urls import path

# importujemy moduł views (plik views.py z tego samego katalogu co plik bieżący)
from . import views

# definiujemy zmienną urlpatterns, która jest listą mapowań adresów URL na nasze widoki
urlpatterns = [
    path("welcome/", views.welcome_view,  name='welcome'),
    path("guests/", views.guest_list, name='guest-list'),
    path("guest/<int:id>/", views.guest_detail, name='guest-detail'),
    path("guest/create/", views.guest_create, name='guest-create'),
    path("guest/<int:id>/update/", views.guest_update, name='guest-update'),
    path("guest/<int:id>/delete/", views.guest_delete, name='guest-delete'),
    path('reservations/', views.reservation_list, name='reservation-list'),
    path('reservation/<int:id>/', views.reservation_detail, name='reservation-detail'),
    path('reservation/create/', views.reservation_create, name='reservation-create'),
    path('reservation/<int:id>/update/', views.reservation_update, name='reservation-update'),
    path('reservation/<int:id>/delete/', views.reservation_delete, name='reservation-delete'),
    path('guest/<int:guest_id>/reservations/', views.guest_reservations, name='guest-reservations'),
    path('reservations/summary/<int:year>/<int:month>/', views.monthly_reservations_summary, name='monthly-reservations-summary'),
    path('reservations/search/', views.search_guest_reservations, name='search-guest-reservations'),
    path('tables/', views.table_list, name='table-list'),
   ]