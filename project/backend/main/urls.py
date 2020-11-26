from rest_framework import routers

from .views import EmployeeViewSet, ItemViewSet

router = routers.SimpleRouter()
router.register(r'employee', EmployeeViewSet)
router.register(r'item', ItemViewSet)

app_name = "main"

urlpatterns = router.urls
