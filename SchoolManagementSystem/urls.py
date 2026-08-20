from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('account/', include("Common.urls")),
    path('api/oboarding/', include('Onboarding.urls')),
    path('_admin/', admin.site.urls),
    path('sy/', include('SalamYusuf.urls')),
    
    ]
