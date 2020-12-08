# coding: utf-8

from rest_framework import routers
from .views import RecipesViewSet


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'recipes', RecipesViewSet)
