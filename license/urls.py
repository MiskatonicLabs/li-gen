from django.urls import path

from . import views

app_name = 'license'

urlpatterns = [
    path('', views.LicenseView.as_view(), name='index'),
]
