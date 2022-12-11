import prog.serializers as prog_serializers
import prog.models as prog_models
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
        'packages': reverse('package', request=request),
        'packagetags': reverse('packagetag', request=request),
        'editions': reverse('edition', request=request),
        'resources': reverse('resource', request=request),
    })


@authentication_classes((SessionAuthentication, BasicAuthentication, TokenAuthentication,))
@permission_classes((IsAuthenticated,))
class ApiPackage(viewsets.ModelViewSet):
    """
    API endpoint that represents a list of objects.
    """
    queryset = prog_models.Package.objects.all()
    serializer_class = prog_serializers.PackageSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields=('name',)
    search_fields=('name',)


@authentication_classes((SessionAuthentication, BasicAuthentication, TokenAuthentication,))
@permission_classes((IsAuthenticated,))
class ApiPackageTag(viewsets.ModelViewSet):
    """
    API endpoint that represents a list of objects.
    """
    queryset = prog_models.PackageTag.objects.all()
    serializer_class = prog_serializers.PackageTagSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields=('key', 'value')
    search_fields=('key', 'value')


@authentication_classes((SessionAuthentication, BasicAuthentication, TokenAuthentication,))
@permission_classes((IsAuthenticated,))
class ApiEdition(viewsets.ModelViewSet):
    """
    API endpoint that represents a list of objects.
    """
    queryset = prog_models.Edition.objects.all()
    serializer_class = prog_serializers.EditionSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields=('name',)
    search_fields=('name',)


@authentication_classes((SessionAuthentication, BasicAuthentication, TokenAuthentication,))
@permission_classes((IsAuthenticated,))
class ApiResource(viewsets.ModelViewSet):
    """
    API endpoint that represents a list of objects.
    """
    queryset = prog_models.Resource.objects.all()
    serializer_class = prog_serializers.ResourceSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields=('text',)
    search_fields=('text',)
