from django.contrib import admin

# Register your models here.
from .models import Quotation_model_1, Quotation_model_2

admin.site.register(Quotation_model_1)

admin.site.register(Quotation_model_2)
