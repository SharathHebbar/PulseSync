
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include('core.urls')),
    path("", include('accounts.urls')),
    path("link/", include('links.urls')),
    path("dashboard/", include('dashboard.urls')),
    path('admin/', admin.site.urls),
    path('stripe/', include('djstripe.urls', namespace='djstripe')),
]
