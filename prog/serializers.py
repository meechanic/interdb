import prog.models as prog_models
from rest_framework import serializers


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = prog_models.Package
        fields = '__all__'


class PackageTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = prog_models.PackageTag
        fields = '__all__'


class EditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = prog_models.Edition
        fields = '__all__'
        ref_name = 'prog_edition'


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = prog_models.Resource
        fields = '__all__'
        ref_name = 'prog_resource'
