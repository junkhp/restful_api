# coding: utf-8

from rest_framework import serializers

from .models import RecipesModel


class RecipesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipesModel()
        fields = '__all__'
