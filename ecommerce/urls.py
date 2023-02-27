from django.contrib import admin
from django.urls import path,include
# To import the variables MEDIA_URL and MEDIA_ROOT from settings:
from django.conf import settings
# To create an unique URL path for our images
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('store.urls')),
    path('cart/',include('cart.urls')),

]

# unique URL path for our images:
urlpatterns +=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
