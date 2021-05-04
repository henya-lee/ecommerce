from django.shortcuts import render

from .cart import Cart

# Create your views here.
def cart_detail (request):
    cart = Cart(request)
    productsstring = ''

    for item in cart:
        product = item['product']
        url = '/%s/%s/' % (product.category.slug, product.slug)
        b = "{'id': '%s', 'title': '%s', 'price': '%s', 'quantity': '%s', 'total_price': '%s'}," % (product.id, product.title, product.price, item['quantity'], item['total_price'])

        productsstring = productsstring + b

    context = {
        'cart': cart,
        'productsstring': productsstring
    }
    return render(request, 'cart.html', context)