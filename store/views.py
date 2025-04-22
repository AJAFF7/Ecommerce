from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category, Profile
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, UpdateUserForm, UserInfoForm
from django import forms
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
import json
from cart.cart import Cart






# Create your views here.

# In store/views.py

# from django.http import HttpResponseServerError

# def home(request):
#     # Intentional mistake: returning an HTTP 500 error response instead of rendering the template
#     return HttpResponseServerError()


def home(request):
    products = Product.objects.all()
    for product in products:
        if product.price and product.sale_price:
            product.discount_percentage = ((product.price - product.sale_price) / product.price) * 100
        else:
            product.discount_percentage = 0
    return render(request, 'home.html', {'products': products})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            
            # Get the cart from sessions
            current_user = Profile.objects.get(user__id=user.id)

            # Get saved cart from database
            saved_cart = current_user.old_cart
            
            # Convert database string to a Python dictionary
            if saved_cart:
                converted_cart = json.loads(saved_cart)
                cart = Cart(request)
                for key, value in converted_cart.items():
                    cart.db_add(product=key, quantity=value)

            messages.success(request, "Logged In Successfully")
            return redirect('home')
        else:
            messages.error(request, "Incorrect Credentials")
            return redirect('login')
    else:
        return render(request, 'login.html', {})




def logout_user(request):
    logout(request)
    messages.success(request, "Logged Out...")
    return redirect('home')




def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Successfully Registered Please Continu")
            return redirect('update_info')
        else:
            # Render the form with errors
            return render(request, 'register.html', {'form': form})
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})
        
        
        
def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)

        if request.method == 'POST':
            user_form = UpdateUserForm(request.POST, instance=current_user)
            password_form = PasswordChangeForm(current_user, request.POST)

            if 'update_profile' in request.POST:
                if user_form.is_valid():
                    user_form.save()
                    login(request, current_user)  # Log the user in again after profile update
                    messages.success(request, "Profile updated!")
                    return redirect('home')  # Redirect to home page after profile update

            elif 'change_password' in request.POST:
                if password_form.is_valid():
                    user = password_form.save()
                    update_session_auth_hash(request, user)  # Update session with the new password
                    messages.success(request, "Password updated!")
                    return redirect('home')  # Redirect to home page after password update
                else:
                    messages.error(request, "Please correct the error below.")
        else:
            user_form = UpdateUserForm(instance=current_user)
            password_form = PasswordChangeForm(current_user)

        return render(request, 'update_user.html', {
            'user_form': user_form,
            'password_form': password_form
        })

    else:
        messages.success(request, "Login first to update!")
        return redirect('home')
        
        
        
def update_info(request):
    if request.user.is_authenticated:
        try:
            current_user_profile = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            messages.error(request, "Profile does not exist.")
            return redirect('home')

        if request.method == 'POST':
            form = UserInfoForm(request.POST, instance=current_user_profile)
            if form.is_valid():
                form.save()
                messages.success(request, "Information updated successfully!")
                return redirect('home')  # Change 'home' if you want to redirect elsewhere
        else:
            form = UserInfoForm(instance=current_user_profile)

        return render(request, 'update_info.html', {'form': form})

    else:
        messages.error(request, "Please log in to update your information.")
        return redirect('home')

        

        
# def home(request):
#     products = Product.objects.all()
#
#     # Annotating products with a discount percentage
#     for product in products:
#         if product.price and product.sale_price:
#             discount_percentage = ((product.price - product.sale_price) / product.price) * 100
#         else:
#             discount_percentage = 0
#         # Adding the discount_percentage to product instance for passing to the template
#         product.discount_percentage = discount_percentage
#
#     return render(request, 'home.html', {'products': products})





def product(request, pk):
    product = Product.objects.get(id=pk)

    return render(request, 'product.html', {'product': product})

def about(request):

    return render(request, 'about.html', {})


# def category(request):
# 	return render(request, 'category.html', {})
def category(request, foo):
    # Replace Hyphens with Spaces
    foo = foo.replace('-', '')
    try:
        # Look Up The Category
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        return render(request, 'category.html', {'products': products, 'category': category})
    except Category.DoesNotExist:
        messages.success(request, "That Category Doesn't Exist")
        return redirect('home')




def search(request):
    query = request.GET.get('q')
    if query:
        search_results = Product.objects.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(category__name__icontains=query)  # FIXED LINE
        ).distinct()
    else:
        search_results = []

    context = {
        'searched': query,
        'search_results': search_results
    }
    return render(request, 'search.html', context)





#def search(request):
#    query = request.GET.get('q')
#    if query:
#        search_results = Product.objects.filter(name__icontains=query)
#    else:
#        search_results = []
#    context = {
#        'searched': query,
#        'search_results': search_results
#    }
#    return render(request, 'search.html', context)


