from django.urls import path
from .views import register, verify_code

urlpatterns = [
    path('signup/', register, name='signup'),
    path('verify_code/', verify_code, name='get_verify_code')
]
