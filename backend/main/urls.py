# from rest_framework import routers
#
# # from .views import EmployeeViewSet, ItemViewSet
# from .views import *
#
# router = routers.SimpleRouter()
# # router.register(r'metadata', EmployeeViewSet)
# router.register(r'item', ItemView)
#
# app_name = "main"
#
# urlpatterns = router.urls
from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('item/', views.ItemView.as_view(), name='get_items'),
    path('item/<pk>/', views.ItemView.as_view(), name='edit_item'),
    path('employee/', views.EmployeeView.as_view(), name='get_employees'),
    path('employee/<pk>/', views.EmployeeView.as_view(), name='edit_employees'),
    path('otss/', views.OTSSView.as_view(), name='get_otss'),
    path('otss/<pk>/', views.OTSSView.as_view(), name='edit_otss'),
    path('unit/', views.UnitView.as_view(), name='get_unit'),
    path('unit/<pk>/', views.UnitView.as_view(), name='edit_unit'),
    path('type/', views.TypeView.as_view(), name='get_type'),
    path('type/<pk>/', views.TypeView.as_view(), name='edit_type'),
]
