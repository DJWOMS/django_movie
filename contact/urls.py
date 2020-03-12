from django.urls import path
from .views import ContactView


urlpatterns = [
    path("", ContactView.as_view(), name="contact")
]
