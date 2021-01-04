# from rest_framework import routers
#
# # from .views import EmployeeViewSet, ItemViewSet
# from .views import *
#
# router = routers.SimpleRouter()
# # router.register(r'employee', EmployeeViewSet)
# router.register(r'item', ItemView)
#
# app_name = "main"
#
# urlpatterns = router.urls
from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('items/', views.ItemView.as_view(), name='get_items'),
    path('items/<pk>', views.ItemView.as_view(), name='edit_item'),
]
