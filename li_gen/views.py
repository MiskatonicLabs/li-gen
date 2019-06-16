from django.shortcuts import render
from rest_framework import permissions, viewsets

from license.models import Category, License
from license.serializers import CategorySerializer, LicenseSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('name')
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = CategorySerializer


class LicenseViewSet(viewsets.ModelViewSet):
    queryset = License.objects.all().order_by('title')
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = LicenseSerializer


def index(request):
    return render(request, 'index.html')
