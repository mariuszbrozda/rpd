from django.core.mail import send_mail, BadHeaderError, EmailMessage, EmailMultiAlternatives
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404, reverse
from .forms import  QuotationForm_1, QuotationForm_2
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib import messages


def emailView(request):
    if request.method == 'GET':
        form_1 = QuotationForm_1()
        form_2 = QuotationForm_2()
    else:
        form_1 = QuotationForm_1(request.POST)
        form_2 = QuotationForm_2(request.POST)
        messages.error(request, 'QUOTATION SENT SUCCESSFULLY !')
        
        if form_1.is_valid() and form_2.is_valid():
            subject = 'QUOTATION REQUEST'
            from_email = form_1.cleaned_data['email_adress']
            full_name = form_1.cleaned_data['full_name']
            phone_number = form_1.cleaned_data['phone_number']
            street_address1 = form_1.cleaned_data['street_address1']
            street_address2 = form_1.cleaned_data['street_address2']
            county = form_1.cleaned_data['county']
           
            
            postcode = form_2.cleaned_data['postcode']
            town_or_city = form_2.cleaned_data['town_or_city']
            Property_type = form_2.cleaned_data['Property_type']
            Bedrooms_nr = form_2.cleaned_data['Bedrooms_nr']
            Bathrooms_nr = form_2.cleaned_data['Bathrooms_nr']
            comments = form_2.cleaned_data['comments']
            
            html_content = render_to_string('mail_template.html',
            {'subject': subject,
            'from_email': from_email,
            'comments': comments,
            'full_name': full_name,
            'phone_number': phone_number,
            'street_address1': street_address1,
            'street_address2': street_address2,
            'county': county,
            
            'postcode': postcode,
            'town_or_city': town_or_city,
            'Property_type': Property_type,
            'Bedrooms_nr': Bedrooms_nr,
            'Bathrooms_nr': Bathrooms_nr,
            'comments': comments,
            }
            )
            try:
                msg = EmailMultiAlternatives(subject, html_content, from_email,  ['rpd.decorators@gmail.com'] )
                msg.attach_alternative(html_content, "text/html")
                msg.send()
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponse(render(request, "index.html", {'form_1': form_1, 'form_2': form_2 }))
             
            
    
 
    form_1 = QuotationForm_1()
    form_2 = QuotationForm_2()  
    messages.error(request, 'QUOTATION SENT SUCCESSFULLY !')
    return render(request, "index.html", {'form_1': form_1, 'form_2': form_2 })

def successView(request):
    return render(request, "index.html", messages.add_message(request, messages.SUCCESS, 'Hello world.'))