from django.urls import path
from .views import ImageAPI,ImageAPIAnyone

urlpatterns = [
    path('', ImageAPI.as_view(), name='image'),
    path('all/', ImageAPIAnyone.as_view(), name='anyone')
]
