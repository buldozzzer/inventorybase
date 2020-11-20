from django.urls import path
from .views import EmployeeViewSet, WealthViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'employee', EmployeeViewSet)
router.register(r'wealth', WealthViewSet)
#router.register(r'component', ComponentViewSet)

app_name = "main"

urlpatterns = router.urls
