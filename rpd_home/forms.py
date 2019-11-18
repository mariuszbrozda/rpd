from django import forms
from .models import Quotation_model_1, Quotation_model_2




class QuotationForm_1(forms.Form):
    full_name = forms.CharField(max_length=15, required=True)
    email_adress = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=10, required=True)
    street_address1 = forms.CharField(max_length=50, required=True)
    street_address2 = forms.CharField(max_length=50, required=False)
    county = forms.CharField(max_length=10, required=True)
    






class QuotationForm_2(forms.Form):
    
    bedrooms_nr= [(i, i) for i in range(1, 6)]
    bathrooms_nr = [(i, i) for i in range(1, 6)]
    property_type = (
        ('House', 'House'),
        ('Apartment','Apartment'),
        ('Duplex','Duplex'),
        ('Bungalow','Bungalow'),
        ('Studio','Studio'),
        ('Other','Other'),
    )
    
    postcode = forms.CharField(max_length=10, required=True)
    town_or_city = forms.CharField(max_length=10, required=True)
    Property_type = forms.TypedChoiceField( choices=property_type)
    Bedrooms_nr = forms.TypedChoiceField( choices=bedrooms_nr)
    Bathrooms_nr = forms.TypedChoiceField( choices=bathrooms_nr)
    comments = forms.CharField(widget=forms.Textarea,max_length=250, required=False)
    
