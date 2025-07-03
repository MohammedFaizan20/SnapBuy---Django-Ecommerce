from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from django.http import HttpResponse
from django.contrib.auth.models import User

def create_admin(request):
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser("admin", "admin@example.com", "yourpassword")
        return HttpResponse("Superuser created!")
    else:
        return HttpResponse("Superuser already exists!")



urlpatterns = [


    path('create-admin/', create_admin),
    # Admin url
    
    path('admin/', admin.site.urls),

    
    # Store app

    path('', include('store.urls')),


    # Cart app

    path('cart/', include('cart.urls')),


    # Account app

    path('account/', include('account.urls')),


    # Payment app

    path('payment/', include('payment.urls')),


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


