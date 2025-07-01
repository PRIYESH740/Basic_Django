from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Order

@login_required
def order_history(request):
    orders = Order.objects.select_related('food').filter(user=request.user).order_by('-order_time')
    return render(request, 'order_history.html', {'orders': orders})