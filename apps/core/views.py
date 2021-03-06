from django.shortcuts import render

from apps.store.models import Product

# Create your views here.
def order_confirmation(request):
    order = Order.objects.get(pk=1)
    return render(request, 'order_confirmation.html')

def frontpage(request):
    products = Product.objects.filter(is_featured=True)

    context = {
        'products': products
    }
    return render(request, 'frontpage.html', context)

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')