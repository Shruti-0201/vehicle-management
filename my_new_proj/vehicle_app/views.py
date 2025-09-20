from django.shortcuts import render, redirect, get_object_or_404
from .models import Vehicle
from .forms import VehicleForm
from django.contrib.auth.decorators import login_required, user_passes_test

# Role check functions
def is_super_admin(user):
    return user.is_superuser

def is_admin(user):
    return user.is_staff

def is_user(user):
    return not user.is_staff and not user.is_superuser

# List vehicles (all roles)
@login_required
def vehicle_list(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'vehicle_app/vehicle_list.html', {'vehicles': vehicles})

# Create vehicle (super admin only)
@login_required
@user_passes_test(is_super_admin)
def vehicle_create(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vehicle_list')
    else:
        form = VehicleForm()
    return render(request, 'vehicle_app/vehicle_form.html', {'form': form})

# Update vehicle (super admin + admin)
@login_required
@user_passes_test(lambda u: is_super_admin(u) or is_admin(u))
def vehicle_update(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    if request.method == 'POST':
        form = VehicleForm(request.POST, instance=vehicle)
        if form.is_valid():
            form.save()
            return redirect('vehicle_list')
    else:
        form = VehicleForm(instance=vehicle)
    return render(request, 'vehicle_app/vehicle_form.html', {'form': form})

# Delete vehicle (super admin only)
@login_required
@user_passes_test(is_super_admin)
def vehicle_delete(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    vehicle.delete()
    return redirect('vehicle_list')

# View details (all roles)
@login_required
def vehicle_detail(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    return render(request, 'vehicle_app/vehicle_detail.html', {'vehicle': vehicle})
