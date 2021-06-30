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
from django.conf import settings
from django.conf.urls.static import static
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

    path('condition/', views.ConditionView.as_view(), name='get_condition'),
    path('condition/<pk>/', views.ConditionView.as_view(), name='edit_condition'),

    path('test/', views.TestView.as_view(), name='test_connection'),

    path('to_excel/', views.ExcelExporterView.as_view(), name='excel_exporter'),

    # path('recognizer/', views.RecognizerView.as_view(), name='recognizer'),

    path('docs/', views.TemplaterView.as_view(), name='g_a_documents'),
    path('docs/<pk>/', views.TemplaterView.as_view(), name='d_r_documents'),

    path('download-docs/', views.DownloadDocsView.as_view(), name='download-documents'),

    path('download-codes/', views.EncodeView.as_view(), name='download-code'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
