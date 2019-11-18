from django.contrib import admin
from django.conf.urls import url

from .views import emailView, successView

urlpatterns = [
    url('admin/', admin.site.urls),
    url('', emailView, name='Home'),
    url('success/', successView, name='success'),
]