from django.urls import path
from . import views
from .views import *

from .forms import * # add o imports at the top of the file


urlpatterns = [
    path('menu/', views.menu, name='menu'),
    path('create-pizza/', create_pizza, name='create_pizza'),
    path('delivery-details/', delivery_details, name='delivery_details'),
    path('order-confirmation/', order_confirmation, name='order_confirmation'),
    path('', views.index, name = "index"),
    path('register/', views.UserSignupView.as_view(), name="register"),
    path('login/',views.LoginView.as_view(template_name="login.html", authentication_form=UserLoginForm)),
    path('logout/', views.logout_user, name="logout"),
    path('view-orders/', view_orders, name='view_orders'),
    path('contact/', views.contact_view, name='contact'),

]