from django.urls import path, include
from account import views

urlpatterns = [
    # auth urls
    path('', include('django.contrib.auth.urls')),

    # dashboard url
    path('', views.dashboard, name='dashboard'),
]
