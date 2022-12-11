import inter.serializers as inter_serializers
import inter.models as inter_models
from django.urls import reverse
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

# Create your views here.

@api_view(['GET'])
@authentication_classes((SessionAuthentication, BasicAuthentication, TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def api_root(request, format=None):
    """
    The entry endpoint of our API.
    """
    return Response({
        'proginfos': reverse('proginfo', request=request),
        'infoinfos': reverse('infoinfo', request=request),
    })


@authentication_classes((SessionAuthentication, BasicAuthentication, TokenAuthentication,))
@permission_classes((IsAuthenticated,))
class ApiProgInfo(viewsets.ModelViewSet):
    """
    API endpoint that represents a list of objects.
    """
    queryset = inter_models.ProgInfo.objects.all()
    serializer_class = inter_serializers.ProgInfoSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields=('prog_package', 'info_infsource')
    search_fields=('prog_package', 'info_infsource')


@authentication_classes((SessionAuthentication, BasicAuthentication, TokenAuthentication,))
@permission_classes((IsAuthenticated,))
class ApiInfoInfo(viewsets.ModelViewSet):
    """
    API endpoint that represents a list of objects.
    """
    queryset = inter_models.InfoInfo.objects.all()
    serializer_class = inter_serializers.InfoInfoSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields=('first_info_infsource', 'second_info_infsource')
    search_fields=('first_info_infsource', 'second_info_infsource')