from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include
from core.views import index, login, orders, cart, contact, about

urlpatterns = [
    path('', index, name="home"),
    path('preview/', include('items.urls') ),
    path('login/', login, name="login"),
    path('orders/', orders, name="orders"),
    path('cart/', cart, name="cart"),
    path('contact/', contact, name="contact"),
    path('about/', about, name="about"),
    path('admin/', admin.site.urls),
    #path('core/', include('core.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
