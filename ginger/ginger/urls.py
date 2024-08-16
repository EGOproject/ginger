
from django.contrib import admin
from django.urls import path
from django.urls import include, path
from core.views import index, contact, login

urlpatterns = [
    path('', index, name="index"),
    path('contact/', contact, name="contact"),
    path('login/', login, name="login"),
    path('admin/', admin.site.urls),
    #path('core/', include('core.urls')),
]
