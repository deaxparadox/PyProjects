from django.urls import path 
from django.views.decorators.csrf import csrf_exempt

from . import views 

urlpatterns = [
    path("cal/", views.Home, name="cal"),
    path("history/", views.History, name="history"),
]
