from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpRequest,JsonResponse
import json
import datetime  

from . models import *
def home(request):
    p = Product.objects.all()

    return render(request,'baby/home.html',{'product':p})

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer,complete = False)
        items  = order.orderitem_set.all()
    else:
        items=[]
        order = {'get_cart_total':0, 'get_cart_items':0}
    return render(request,'baby/cart.html',{'items':items,'order':order}) 

def  updateItem(request): 
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:',action)
    print('productId',productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer = customer,complete = False)

    orderItem, created = OrderItem.objects.get_or_create(order=order,product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <=0 :
        orderItem.delete()

    return JsonResponse('Item was added',safe=False)


def checkout(request):
    return render(request,'baby/checkout.html')


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    customer = request.user.customer
    
    order, created = Order.objects.get_or_create(customer = customer,complete = False)
    order.transaction_id = transaction_id
    order.complete = True
    order.save()

    address = request.POST["address"]
    city = request.POST["city"]
    state = request.POST["state"]
    zipcode = request.POST["zip"]
    s =  ShippingAddress(
        customer = customer,
        order  = order,
        address = address,
        city = city,
        state = state,
        zipcode = zipcode)
    s.save()
    return render(request,'baby/ordered.html',{'order':order,'s':s})
