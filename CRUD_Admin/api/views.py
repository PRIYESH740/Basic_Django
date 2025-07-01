# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from api.models import FoodItem
from .forms import FoodItemForm

# Helper to check admin
def is_admin(user):
    return user.is_superuser

@login_required
@user_passes_test(is_admin)
def food_list(request):
    foods = FoodItem.objects.all()
    return render(request, 'food_list.html', {'foods': foods})

@login_required
@user_passes_test(is_admin)
def food_create(request):
    if request.method == 'POST':
        form = FoodItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('food_list')
    else:
        form = FoodItemForm()
    return render(request, 'food_form.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def food_update(request, pk):
    food = get_object_or_404(FoodItem, pk=pk)
    if request.method == 'POST':
        form = FoodItemForm(request.POST, request.FILES, instance=food)
        if form.is_valid():
            form.save()
            return redirect('food_list')
    else:
        form = FoodItemForm(instance=food)
    return render(request, 'food_form.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def food_delete(request, pk):
    food = get_object_or_404(FoodItem, pk=pk)
    if request.method == 'POST':
        food.delete()
        return redirect('food_list')
    return render(request, 'food_confirm_delete.html', {'food': food})
