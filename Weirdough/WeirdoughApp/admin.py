from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Pizza)
admin.site.register(Order)
admin.site.register(Size)
admin.site.register(Cheese)
admin.site.register(Sauce)
admin.site.register(PredefinedPizza)