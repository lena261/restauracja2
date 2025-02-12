# Create your views here.
# kod umieszczamy w pliku views.py wybranej aplikacji

from django.http import Http404, HttpResponse
import datetime
from django.shortcuts import render, redirect, get_object_or_404
from .forms import GuestNameForm, ReservationForm
from .models import GuestName, Reservation, Table 
from django.db.models import Count
from django.utils.timezone import now
from datetime import datetime
from django.db.models.functions import TruncMonth


def welcome_view(request):
    return render(request,
                  "myapp/base.html")


def guest_list(request):
    # pobieramy wszystkie obiekty Person z bazy poprzez QuerySet
    if request.method == 'POST':
        guests = GuestName.objects.filter(lastname__icontains=request.POST['phrase'])
    else:
        guests = GuestName.objects.all()

    return render(request,
                  "myapp/guest/list.html",
                  {'guests': guests})

def guest_detail(request, id):
    # pobieramy konkretny obiekt Person
    guest = GuestName.objects.get(id=id)

    return render(request,
                  "myapp/guest/detail.html",
                  {'guest': guest})

def guest_create(request):
    if request.method == 'POST':
        form = GuestNameForm(request.POST)
        if form.is_valid():
            # zapisujemy obiekt do bazy
            guest = form.save()
            # po dodaniu nastąpi przekierowanie do strony szczegółów tego obiektu
            return redirect('guest-detail', guest.id)
    else:
        form = GuestNameForm()

    return render(request,
                'myapp/guest/create.html',
                {'form': form})


def guest_update(request, id):
    try:
        guest = GuestName.objects.get(id=id)
    except GuestName.DoesNotExist:
        raise Http404("Obiekt Guest o podanym id nie istnieje")

    if request.method == 'POST':
        form = GuestNameForm(request.POST, instance=guest)
        if form.is_valid():
            # zapisujemy obiekt do bazy
            guest = form.save()
            # po dodaniu nastąpi przekierowanie do strony szczegółów tego obiektu
            return redirect('guest-detail', guest.id)
    else:
        form = GuestNameForm(instance=guest)
        
    return render(request,
                    'myapp/guest/update.html',
                    {'form': form})


def guest_delete(request, id):
    try:
        guest = GuestName.objects.get(id=id)
        guest.delete()
    except GuestName.DoesNotExist:
        raise Http404("Obiekt Guest o podanym id nie istnieje")

    return redirect('guest-list')

# Lista rezerwacji
def reservation_list(request):
    reservations = Reservation.objects.all()
    return render(request, 'myapp/reservation/list.html', {'reservations': reservations})

# Szczegóły rezerwacji
def reservation_detail(request, id):
    reservation = get_object_or_404(Reservation, id=id)
    return render(request, 'myapp/reservation/detail.html', {'reservation': reservation})

# Tworzenie nowej rezerwacji
def reservation_create(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservation-list')
    else:
        form = ReservationForm()
    return render(request, 'myapp/reservation/form.html', {'form': form})

# Edytowanie rezerwacji
def reservation_update(request, id):
    reservation = get_object_or_404(Reservation, id=id)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('reservation-detail', id=reservation.id)
    else:
        form = ReservationForm(instance=reservation)
    return render(request, 'myapp/reservation/form.html', {'form': form})

# Usuwanie rezerwacji
def reservation_delete(request, id):
    reservation = get_object_or_404(Reservation, id=id)
    if request.method == 'POST':
        reservation.delete()
        return redirect('reservation-list')
    return render(request, 'myapp/reservation/confirm_delete.html', {'reservation': reservation})

# Widok rezerwacji dla danego klienta
def guest_reservations(request, guest_id):
    guest = get_object_or_404(GuestName, id=guest_id)
    reservations = Reservation.objects.filter(lastname=guest)
    return render(request, 'myapp/reservation/guest_reservations.html', {'guest': guest, 'reservations': reservations})

# Widok podsumowania rezerwacji z miesiąca
def monthly_reservations_summary(request, year, month):
    reservations = Reservation.objects.filter(dateTime__year=year, dateTime__month=month)
    total_reservations = reservations.count()

    # Poprawione odniesienie do pola lastname (np. firstname lub lastname)
    reservations_by_guest = reservations.values('lastname__firstname', 'lastname__lastname').annotate(total=Count('id'))

    return render(request, 'myapp/reservation/monthly_summary.html', {
        'reservations': reservations,
        'total_reservations': total_reservations,
        'reservations_by_guest': reservations_by_guest,
        'year': year,
        'month': month,
    })



# Widok do wyszukiwania rezerwacji danego gościa
def search_guest_reservations(request):
    query = request.GET.get('query')  # Pobierz zapytanie z pola wyszukiwania
    reservations = []

    if query:
        # Wyszukiwanie rezerwacji według imienia lub nazwiska (case-insensitive)
        reservations = Reservation.objects.filter(
            lastname__firstname__icontains=query
        ) | Reservation.objects.filter(
            lastname__lastname__icontains=query
        )

    return render(request, 'myapp/reservation/search_guest_reservations.html', {
        'reservations': reservations,
        'query': query,
    })

from django.shortcuts import render
from .models import Table

# Widok wyświetlający listę stolików
def table_list(request):
    tables = Table.objects.all()  # Pobiera wszystkie stoliki z bazy danych
    return render(request, 'myapp/table/list.html', {'tables': tables})