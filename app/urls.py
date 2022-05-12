from django.urls import path
from .views import ImageAPI,ImageAPIAnyone, ChangePlan

urlpatterns = [
    # route for authenticated users
    path('', ImageAPI.as_view(), name='image'),
    # route where plan or tiers can be changed
    path('plan/', ChangePlan.as_view(), name='plan'),
    # route for anyone
    path('all/', ImageAPIAnyone.as_view(), name='anyone')
]
