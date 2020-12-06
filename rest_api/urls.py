# coding: utf-8

from rest_framework import routers
from .views import RecipesViewSet


router = routers.DefaultRouter()
router.register(r'recipes', RecipesViewSet)
