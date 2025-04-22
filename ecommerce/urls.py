
from django.contrib import admin
from django.urls import path
from . import settings
from django.conf.urls.static import static

from store.views import home
from store.views import login_user
from store.views import logout_user
from store.views import register_user
from store.views import update_user
from store.views import update_info
from store.views import product
from store.views import about
from store.views import category
from store.views import search


from cart.views import cart_summary
from cart.views import cart_add
from cart.views import cart_delete
from cart.views import cart_update

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    #path('product/', product, name='product'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register_user, name='register'),
    path('update_user/', update_user, name='update_user'),
    path('update_info/', update_info, name='update_info'),
    path('product/<int:pk>/', product, name='product'),
    path('about/', about, name='about'),
    path('category/<str:foo>', category, name='category'),
    path('search/', search, name='search'),


    path('cart/', cart_summary, name="cart_summary"),
    path('cart/add/', cart_add,name="cart_add"),
    # path( 'cart/delete/', cart_delete, name="cart_delete"),
    path('cart/delete/', cart_delete, name='cart_delete'),
    path( 'cart/update/', cart_update, name="cart_update"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
