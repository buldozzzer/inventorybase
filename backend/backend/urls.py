from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('inventorybase/admin/', admin.site.urls),
    # path('inventorybase/api/v1/', include('main.urls')),
    # path('inventorybase/', include('main.index_url')),
    path('admin/', admin.site.urls),
    path('api/v1/', include('main.urls')),
    path('inventorybase/', include('main.index_url')),
]
