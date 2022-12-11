from django.contrib import admin
from import_export import resources
import info.models as info_models
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class InfsourceResource(resources.ModelResource):

    class Meta:
        model = info_models.Infsource


class InfsourceTagResource(resources.ModelResource):

    class Meta:
        model = info_models.InfsourceTag


class EditionResource(resources.ModelResource):

    class Meta:
        model = info_models.Edition


class ResourceResource(resources.ModelResource):

    class Meta:
        model = info_models.Resource


@admin.register(info_models.Infsource)
class CategoryAdmin(ImportExportModelAdmin):
    resource_class = InfsourceResource


@admin.register(info_models.InfsourceTag)
class CategoryAdmin(ImportExportModelAdmin):
    resource_class = InfsourceTagResource


@admin.register(info_models.Edition)
class CategoryAdmin(ImportExportModelAdmin):
    resource_class = EditionResource


@admin.register(info_models.Resource)
class CategoryAdmin(ImportExportModelAdmin):
    resource_class = ResourceResource
