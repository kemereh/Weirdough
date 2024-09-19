from django import forms 
from .models import Pizza, Order, Sauce, Cheese, Size, PredefinedPizza
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm, ModelChoiceField
from .models import User
from django.db import transaction

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Email'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'

class UserSignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_admin = False
        user.email = self.cleaned_data['username']
        user.save()
        return user

class PizzaForm(forms.ModelForm):
    ToppingChoices = [
        ('Pepperoni', 'Pepperoni'),
        ('Chicken', 'Chicken'),
        ('Ham', 'Ham'),
        ('Pineapple', 'Pineapple'),
        ('Peppers', 'Peppers'),
        ('Mushrooms', 'Mushrooms'),
        ('Onions', 'Onions'),
    ]
    CrustChoices = [
        ('---------------', '---------------'),
        ('Normal', 'Normal'),
        ('Thin', 'Thin'),
        ('Thick', 'Thick'),
        ('Gluten Free', 'Gluten Free'),
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['sauce'].queryset = Sauce.objects.all()
        self.fields['cheese'].queryset = Cheese.objects.all()
        self.fields['size'].queryset = Size.objects.all()


    

    crust = forms.ChoiceField(choices=CrustChoices)
    toppings = forms.MultipleChoiceField(choices=ToppingChoices, widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = PredefinedPizza
        fields = ['size', 'sauce', 'cheese', 'crust', 'toppings']
    class Meta:
        model = Pizza
        fields = ['size', 'sauce', 'cheese', 'crust', 'toppings']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'delivery_address', 'card_number', 'cvv', 'expiry_date']

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)