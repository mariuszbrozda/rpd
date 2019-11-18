
from django.db import models


# Create your models here.
class Quotation_model_1(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    email_adress = models.CharField(max_length=20, blank=False) 
    phone_number = models.CharField(max_length=20, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=False)
    county = models.CharField(max_length=40, blank=False)
    
    



class Quotation_model_2(models.Model):
    
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
    
    
    postcode = models.CharField(max_length=20, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    Property_type = models.CharField( max_length=10, choices=property_type)
    Bedrooms_nr = models.CharField( max_length=10, choices=bedrooms_nr)
    Bathrooms_nr = models.CharField(max_length=10,  choices=bathrooms_nr)
    comments = models.CharField(max_length=300, blank=False)  
    
    
    
    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)

  