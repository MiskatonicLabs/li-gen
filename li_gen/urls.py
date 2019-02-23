from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from . import views

app_name = 'li_gen'

router = routers.DefaultRouter()
router.register('categories', views.CategoryViewSet)
router.register('licenses', views.LicenseViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('license/', include('license.urls'), name='license'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
