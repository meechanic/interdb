from django.db import models
from django.urls import reverse
import prog.models as prog_models
import info.models as info_models

# Create your models here.

class ProgInfo(models.Model):
    prog_package = models.ForeignKey(prog_models.Package, blank=False, related_name='prog_package', on_delete=models.CASCADE,)
    info_infsource = models.ForeignKey(info_models.Infsource, blank=False, related_name='info_infsource', on_delete=models.CASCADE,)
    connection_kind = models.TextField(blank=True)

    def __str__(self):
        return ' '.join([self.prog_package.name, self.info_infsource.name, self.connection_kind])

    def __unicode__(self):
        return self.__str__()

    def get_absolute_url(self):
        return reverse('prog-info-view', kwargs={'pk': self.id})

    class Meta:
        ordering = ['prog_package', 'info_infsource', 'connection_kind']