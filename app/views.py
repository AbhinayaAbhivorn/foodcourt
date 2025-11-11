from django.shortcuts import render, redirect
from .models import FoodItem, Order
from .forms import OrderForm

# Home page for users
def home(request):
    items = FoodItem.objects.all()
    return render(request, 'useritems.html', {'items': items})
    

# Display all available food items
def user_items(request):
    items = FoodItem.objects.all()
    return render(request, 'useritems.html', {'items': items})
def order_list(request):
    orders=Order.objects.all()
    return render(request, 'orderlist.html', {'orders':orders})


# Order Now page
def order_now(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_items')
    else:
        form = OrderForm()
    return render(request, 'ordernow.html', {'form': form})

