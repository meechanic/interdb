import info.models as info_models
from rest_framework import serializers


class InfsourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = info_models.Infsource
        fields = '__all__'


class InfsourceTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = info_models.InfsourceTag
        fields = '__all__'


class EditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = info_models.Edition
        fields = '__all__'


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = info_models.Resource
        fields = '__all__'
