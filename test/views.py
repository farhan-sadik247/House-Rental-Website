from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
import random
# import csv
# from django.http import JsonResponse, Http404, HttpResponse
from django.contrib import messages
from django.conf import settings
from django.db.models import Q
from .models import Manush, House, Cart, Cart_item
from .forms import HouseForm, RegistrationForm, SearchForm


# Create your views here.
def findHome(request):
    if request.method == 'POST':
        loc = request.POST['location'] 
        price1 = None if request.POST['price1'] == '' else int(request.POST['price1'])
        price2 = None if request.POST['price2'] == '' else int(request.POST['price2'])
        gender = request.POST['gender']
        type = None if request.POST['type'] == '' else request.POST['type']
        if price1 == None:
            price1 = 0
        if price2== None:
            price2 = 99999999999999
        
        if type == None:
            house = House.objects.filter(Q(location__contains= loc) & Q(price__gte = price1) & Q(price__lte= price2) & Q(gender__contains = gender))
        else:
            house = House.objects.filter(Q(location__contains= loc) & Q(price__gte = price1) & Q(price__lte= price2) & Q(type__contains = type) & Q(gender__contains = gender))
        print(request.POST,price1,price2)
    return render(request, 'all_houses.html', {
            'products': house,
            # 'searched': searched,``
            'title': 'All Available Houses Right Now' if len(house) > 0 else 'Sorry, Nothing Matches Your Search'
                    })
def home(request):
    house = House.objects.all()  
    form = SearchForm()                                                    

    house_list = list(house)

    # Randomly suffling      
    random.shuffle(house_list)   
    house = House.objects.all()    
    return render(
        request, 'home.html',
        {
            'Houses': house_list,
            'request': request,            
        })

def house(request, house_id):
    house = House.objects.get(pk = house_id)
    in_cart = False
    if request.user.is_authenticated:
        cart_items = Cart_item.objects.filter(cart=Cart.objects.get(manush=request.user))
        for item in cart_items:
            if item.house == house:
                in_cart = True
                break

        print(in_cart)
    else:
        cart_items = []
    return render(request, 'house.html', {
        'product': house,
        'in_cart': in_cart
        })

def add_house(request, manush_id):
    if request.user.is_authenticated == False:
        messages.error(request, 'You do not have the permission to view that page')
        return redirect('home')
    if request.method == 'POST':
        form = HouseForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.manush = Manush.objects.get(pk = manush_id)
            flat_type = form.cleaned_data.get("flat_type")
            form.type = flat_type
            product.save()
            form.save()                                                                        
            messages.success(request, 'House has been added!')
            return redirect('home')           
    else:
        form = HouseForm()
    return render(request, 'house_form.html', {
        'form': form,
        'button_txt': 'Add'
        })

def update_house(request, house_id):
    house = House.objects.get(id=house_id)                                
    form = HouseForm(instance=house)
    if request.method == 'POST':      
        form = HouseForm(request.POST, request.FILES, instance=house)   
        if form.is_valid():
            form.save()                                                         
            messages.success(request, 'House attributes has been updated!')
            return redirect('home')
    return render(request, 'house_form.html', {
        'form': form,
        'button_txt': 'Update'
        })

def manage_houses(request):                                     
    products = House.objects.filter(manush=request.user)                               
    # Deleting house
    if request.method == 'POST':
        product = House.objects.get(id = request.POST['house_id'])          
        product.delete()                                                          
        return redirect('manage_houses')
    return render(request, 'manage_houses.html', {
        'houses': products
    })

def bookmark(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            item_id = request.POST['item_id']
            print(item_id)
            Cart_item.objects.get(id=item_id).delete()        
            return redirect('bookmark')
        user = request.user
        cart_obj = Cart.objects.get(manush=user)                    
        cart_items = Cart_item.objects.filter(cart=cart_obj)               
        items = []                                  
        for item in cart_items:
            temp = {}
            temp['item'] = item
            items.append(temp)
        return render(request, 'bookmark.html', {
            'cart_items': items,
            'user': user,
        })
    else:
        messages.error(request, 'You do not have the permission to view that page!')
        return redirect('home')
    
def login_manush(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        check = authenticate(request, username=username, password=password)
        if check is not None:
            login(request, check)
            return redirect('home')
        else:
            messages.error(request, ('Error loging in !!!'))
            return redirect('login')    
    else:
        return render(request, 'login.html', {})
    
def logout_manush(request):
    logout(request)
    messages.warning(request, 'You were logged out')
    return redirect('home')

def register_manush(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()                                                                             
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            bookmarking = Cart.objects.create(manush=user)                                            
            messages.success(request, f'You are now logged in as {request.user.username}')
            return redirect('home')
        else:
            print(form.error_messages)
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {
        'form': form,
        'info': 'Register'
        })

def update_profile(request):  
    form = RegistrationForm(instance = request.user)

    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()                                                                            
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect('home')
    
    return render(request, 'registration.html', {
        'form': form,
        'info': 'Update'
    })
    
@login_required
def add_bookmark(request):
    if request.method == 'POST':
        print(request.POST)
        house_pk = request.POST.get('house_pk')
        house_obj = House.objects.get(pk=house_pk)

        cart_obj = Cart.objects.get(manush = request.user.pk)                                                       
        cart_item = Cart_item.objects.create(cart=cart_obj, house=house_obj)       
        cart_item.save()

        return redirect('house', house_id = house_pk)
    else:
        print("\nSOMETHING WENT WRONGE\n")
    

def all_house(request):
    searched = False
    house = House.objects.all() 
    if request.method == 'POST':
        form = SearchForm(request.POST, request.FILES)
        if form.is_valid():
            loc = form.cleaned_data['location'] 
            price1 = form.cleaned_data['price1']
            gender = form.cleaned_data['gender']
            price2 = form.cleaned_data['price2']
            type = form.cleaned_data['type']
            if price1 == None:
                price1 = 0
            if price2== None:
                price2 = 99999999999999
            
            if type == None:
                house = House.objects.filter(Q(location__contains= loc) & Q(price__gte = price1) & 
                                             Q(price__lte= price2) & Q(gender__contains = gender))
            else:
                house = House.objects.filter(Q(location__contains= loc) & Q(price__gte = price1) & 
                                             Q(price__lte= price2) & Q(type__contains = type) & Q(gender__contains = gender))

        return render(request, 'all_houses.html', {
            'products': house,
            'searched': searched,
            'title': 'All Available Houses Right Now' if len(house) > 0 else 'Sorry, Nothing Matches Your Search'
                    })
    else:
        form = SearchForm()
        return render(request, 'search_form.html', {'form': form})

