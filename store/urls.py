from django.contrib import admin
from django.urls import path
from .views.home import Index , store , productView, search
from .views.signup import Signup
from .views.login import Login , logout
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView
from .middlewares.auth import  auth_middleware
from .views.saleorder import sales_order_form,sales_order_success,create_sales_order,search_retail,search_product
urlpatterns = [
    path('', Index.as_view(), name='homepage'),
     path('search', search, name='Search'),
    path('store', store , name='store'),
   path("products/<int:id>", productView, name="ProductView"),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout , name='logout'),
    path('cart', auth_middleware(Cart.as_view()) , name='cart'),
    path('check-out', CheckOut.as_view() , name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
      path('sales-order/', sales_order_form, name='sales_order_form'),
    path('create-sales-order/',create_sales_order, name='create_sales_order'),
    path('search-product/', search_product, name='search_product'),
    path('search-retail/', search_retail, name='search_retail'),
    path('sales-order/success/', sales_order_success, name='sales_order_success'),
]