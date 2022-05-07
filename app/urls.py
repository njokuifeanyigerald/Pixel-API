from django.urls import path
from .views import ImageAPI

urlpatterns = [
    path('', ImageAPI.as_view(), name='image')
]
