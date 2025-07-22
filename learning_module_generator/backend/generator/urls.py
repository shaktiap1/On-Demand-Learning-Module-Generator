from django.urls import path
from .views import module_form

urlpatterns = [
    path("", module_form, name="module_form"),
]
