from django.shortcuts import render, redirect
from .models import FoodItem, Order
from .forms import OrderForm

# Home page for users
def home(request):
    return render(request, 'foodcourt/home.html')

# Display all available food items
def user_items(request):
    items = FoodItem.objects.all()
    return render(request, 'foodcourt/user_items.html', {'items': items})

# Order Now page
def order_now(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_items')
    else:
        form = OrderForm()
    return render(request, 'foodcourt/order.html', {'form': form})

# Admin order list page
def admin_orders(request):
    orders = Order.objects.all().order_by('-created_at')
    return render(request, 'foodcourt/admin_orders.html', {'orders': orders})
