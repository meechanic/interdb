from django.contrib import admin
from import_export import resources
import inter.models as inter_models
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class ProgInfoResource(resources.ModelResource):

    class Meta:
        model = inter_models.ProgInfo


@admin.register(inter_models.ProgInfo)
class CategoryAdmin(ImportExportModelAdmin):
    resource_class = ProgInfoResource


class InfoInfoResource(resources.ModelResource):

    class Meta:
        model = inter_models.InfoInfo


@admin.register(inter_models.InfoInfo)
class CategoryAdmin(ImportExportModelAdmin):
    resource_class = InfoInfoResource