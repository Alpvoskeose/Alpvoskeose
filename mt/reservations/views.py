from django.shortcuts import render, get_object_or_404, redirect
from .models import Reservation, ReservationStatus
from .forms import ReservationForm, ReservationStatusForm

def reservation_list(request):
    reservations = Reservation.objects.all()
    return render(request, 'reservations/reservation_list.html', {'reservations': reservations})

def reservation_create(request):
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservation_list')
    else:
        form = ReservationForm()
    return render(request, 'reservations/reservation_form.html', {'form': form})

def reservation_edit(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    if request.method == "POST":
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('reservation_list')
    else:
        form = ReservationForm(instance=reservation)
    return render(request, 'reservations/reservation_form.html', {'form': form})

def reservation_delete(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    if request.method == "POST":
        reservation.delete()
        return redirect('reservation_list')
    return render(request, 'reservations/reservation_confirm_delete.html', {'reservation': reservation})

def status_list(request):
    statuses = ReservationStatus.objects.all()
    if request.method == "POST":
        form = ReservationStatusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('status_list')
    else:
        form = ReservationStatusForm()
    return render(request, 'reservations/status_list.html', {'statuses': statuses, 'form': form})
