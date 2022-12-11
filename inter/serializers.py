import inter.models as inter_models
from rest_framework import serializers


class ProgInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = inter_models.ProgInfo
        fields = '__all__'
