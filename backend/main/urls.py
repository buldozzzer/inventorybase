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

    path('category/', views.CategoryView.as_view(), name='get_category'),
    path('category/<pk>/', views.CategoryView.as_view(), name='edit_category'),

    path('location/', views.LocationView.as_view(), name='get_category'),
    path('location/<pk>/', views.LocationView.as_view(), name='edit_category'),
    # урлы для тестов, но с теми же представлениями
    path('test_item/', views.ItemView.as_view(), name='get_items'),
    path('test_item/<pk>/', views.ItemView.as_view(), name='edit_item'),

    path('test_employee/', views.EmployeeView.as_view(), name='get_employees'),
    path('test_employee/<pk>/', views.EmployeeView.as_view(), name='edit_employees'),

    path('test_otss/', views.OTSSView.as_view(), name='get_otss'),
    path('test_otss/<pk>/', views.OTSSView.as_view(), name='edit_otss'),

    path('test_unit/', views.UnitView.as_view(), name='get_unit'),
    path('test_unit/<pk>/', views.UnitView.as_view(), name='edit_unit'),

    path('test_type/', views.TypeView.as_view(), name='get_type'),
    path('test_type/<pk>/', views.TypeView.as_view(), name='edit_type'),

    path('test_category/', views.CategoryView.as_view(), name='get_category'),
    path('test_category/<pk>/', views.CategoryView.as_view(), name='edit_category'),

    path('test_location/', views.LocationView.as_view(), name='get_category'),
    path('test_location/<pk>/', views.LocationView.as_view(), name='edit_category'),
]
