from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/account/', include("Common.urls")),
    path('api/onboarding/', include('Onboarding.urls')),
    path('api/_admin/', admin.site.urls),
    path('api/sy/', include('SalamYusuf.urls')),
    
    ]
