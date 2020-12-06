from django.db.models.query import QuerySet
import django_filters
from rest_framework import viewsets, filters

from .models import RecipesModel
from .serializer import RecipesSerializer


# Create your views here.
class RecipesViewSet(viewsets.ModelViewSet):
    queryset = RecipesModel.objects.all()
    print(queryset)
    serializer_class = RecipesSerializer
    print(serializer_class)
