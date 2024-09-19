from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import *
from .forms import PizzaForm, OrderForm
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import * 
from .models import *
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from django.core.exceptions import ValidationError
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender_email = form.cleaned_data['email']
            return render(request, 'thank_you.html')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

class UserLoginView(LoginView):
    template_name='login.html'

    def get_success_url(self):
        return reverse_lazy('index')


def logout_user(request):
    logout(request)
    return redirect("index")


class UserSignupView(CreateView):
    model = User
    form_class = UserSignupForm
    template_name = 'user_signup.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')
# Create your views here.

def index(request):
    return render(request, 'index.html')

def menu(request):
    pizza = Pizza.objects.all()
    predefined_pizza = PredefinedPizza.objects.all()
    return render(request, 'menu.html', {'predefined_pizza': predefined_pizza, 'pizza': pizza})

def customize(request, predefined_pizza_id):
    pizza = PredefinedPizza.objects.get(pk=predefined_pizza_id)
    if request.method == 'POST':
        # Handle customization form submission
        # Create an order with the customized pizza
        # Redirect to order confirmation page
        pass
    else:
        form = PizzaForm()  # Create an instance of the PizzaForm
        # Pass the form and the pizza object to the template
    return render(request, 'customize.html', {'form': form, 'pizza': pizza})


def create_pizza(request):
    if request.method == 'POST':
        form = PizzaForm(request.POST)
        if form.is_valid():
            pizza = form.save()
            request.session['pizza_id'] = pizza.id
            return redirect('delivery_details')
    else:
        form = PizzaForm()
    return render(request, 'create_pizza.html', {'form': form})


@login_required
def delivery_details(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.pizza_id = request.session.get('pizza_id')
            pizza = get_object_or_404(Pizza, id=order.pizza_id)
            order.pizza = pizza
            order.save()
            return redirect('order_confirmation')
    else:
        form = OrderForm()
    return render(request, 'delivery_details.html', {'form': form})


    
def order_confirmation(request):
    pizza_id = request.session.get('pizza_id')
    if pizza_id:
        pizza = Pizza.objects.get(id=pizza_id)
        order = Order.objects.filter(user=request.user, pizza=pizza).first()
        if order:
            order_date = order.order_date
            del request.session['pizza_id']
            return render(request, 'order_confirmation.html', {'pizza': pizza, 'order_date': order_date})
    return redirect('/')

    

@login_required
def view_orders(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'view_orders.html', {'orders': orders})