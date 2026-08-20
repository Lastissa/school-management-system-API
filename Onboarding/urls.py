from . import views
from django.urls import path

urlpatterns = [
    path('student/', views.StudentApplication.as_view(), name = "onboarding_student")
]
