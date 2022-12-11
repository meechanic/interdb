from django.contrib import admin
from import_export import resources
import prog.models as prog_models
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class PackageResource(resources.ModelResource):

    class Meta:
        model = prog_models.Package


class PackageTagResource(resources.ModelResource):

    class Meta:
        model = prog_models.PackageTag


class EditionResource(resources.ModelResource):

    class Meta:
        model = prog_models.Edition


class ResourceResource(resources.ModelResource):

    class Meta:
        model = prog_models.Resource


@admin.register(prog_models.Package)
class PackageAdmin(ImportExportModelAdmin):
    resource_class = PackageResource


@admin.register(prog_models.PackageTag)
class PackageAdmin(ImportExportModelAdmin):
    resource_class = PackageTagResource


@admin.register(prog_models.Edition)
class EditionAdmin(ImportExportModelAdmin):
    resource_class = EditionResource


@admin.register(prog_models.Resource)
class ResourceAdmin(ImportExportModelAdmin):
    resource_class = ResourceResource
