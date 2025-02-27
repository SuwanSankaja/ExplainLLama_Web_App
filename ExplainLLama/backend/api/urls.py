from django.urls import path
from .views import fix_code

urlpatterns = [
    path('fix_code/', fix_code, name="fix_code"),
]
