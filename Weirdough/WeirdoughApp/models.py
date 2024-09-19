from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, User
from django.core.validators import MinLengthValidator, MaxLengthValidator, RegexValidator
from django.core.exceptions import ValidationError
#... any other imports

class UserManager(BaseUserManager):


    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    email = models.EmailField('Email', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()


class Size(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Cheese(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Sauce(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class PredefinedPizza(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    toppings = models.CharField(max_length=255)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    sauce = models.ForeignKey(Sauce, on_delete=models.CASCADE)
    cheese = models.ForeignKey(Cheese, on_delete=models.CASCADE)
    crust = models.CharField(max_length=50)

    def __str__(self):
        return self.name 
    
class Pizza(models.Model):
    toppings = models.CharField(max_length=50)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    sauce = models.ForeignKey(Sauce, on_delete=models.CASCADE)
    cheese = models.ForeignKey(Cheese, on_delete=models.CASCADE)
    crust = models.CharField(max_length=50)

def validate_expiry_date(value):
    if not value or len(value) != 5:
        raise ValidationError('Expiry date must be in the format MM/YY.')
    
    try:
        month, year = value.split('/')
        month = int(month)
        year = int(year)
    except ValueError:
        raise ValidationError('Expiry date must be in the format MM/YY.')
    
    if not (1 <= month <= 12 and 0 <= year <= 99):
        raise ValidationError('Expiry date is not valid.')
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    delivery_address = models.CharField(max_length=55)
    card_number = models.CharField(max_length=16, validators=[MinLengthValidator(16), MaxLengthValidator(16), RegexValidator(r'^\d{16}$', message='Card number must contain only numeric characters.')])
    cvv = models.CharField(max_length=3, validators=[MinLengthValidator(3), MaxLengthValidator(3), RegexValidator(r'^\d{3}$', message='CVC must contain only numeric characters.')])
    expiry_date = models.CharField(max_length=5, validators=[validate_expiry_date])
    order_date = models.DateTimeField(auto_now_add=True)