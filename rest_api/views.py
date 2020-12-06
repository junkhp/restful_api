from django.db.models.query import QuerySet
import django_filters
from rest_framework import viewsets, filters

from .models import RecipesModel
from .serializer import RecipesSerializer


# Create your views here.
class RecipesViewSet(viewsets.ModelViewSet):
    # queryset = {'recipes': RecipesModel.objects.all()}
    queryset = RecipesModel.objects.all()

    serializer_class = RecipesSerializer
    # queryset = {'recipes': queryset}
    # print(serializer_class)
