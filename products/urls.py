from django.urls import path
from products.views import mainPage

urlpatterns = [
    path("/", mainPage)
]