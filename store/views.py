from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from django.db.models import Q




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
            messages.success(request, ("Logged In Successfuly"))
            return redirect('home')
        else:
            messages.success(request, ("Incorrect Credintial"))
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
            messages.success(request, "Successfully Registered! Welcome!")
            return redirect('home')
        else:
            # Render the form with errors
            return render(request, 'register.html', {'form': form})
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})

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


