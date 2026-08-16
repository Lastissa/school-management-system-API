from django.urls import path, include
from . import views

urlpatterns = [
    path('_admin/<path:email>/', views.CreateSYAcc.as_view()),
    path('_admin/<str:email>/<str:password>/<str:sy_secret_incoming>/', views.CreateSYAcc.as_view())
]
