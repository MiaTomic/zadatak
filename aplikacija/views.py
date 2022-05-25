from multiprocessing import context
from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json
from django.views import View
from django.views.generic import DetailView


def trgovina(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items= order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {"get_cart_total":0, "get_cart_items":0}
        cartItems = order["get_cart_items"]
    products = Product.objects.all()
    context = {
        "products" : products,
        "cartItems": cartItems
    }
    return render (request, "aplikacija/trgovina.html", context)



def kosarica(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {"get_cart_total":0, "get_cart_items":0}
        cartItems = order["get_cart_items"]
    context = {
        "items": items,
        "order": order,
        "cartItems": cartItems
    }
    return render (request, "aplikacija/kosarica.html", context)


def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)

def thankYou(request):
    context ={} 
    return render(request, "aplikacija/hvala.html", context)

def vise(request,pk):
    
    product = Product.objects.get(pk=pk)
    return render(request, "aplikacija/vise.html", {"product":product})