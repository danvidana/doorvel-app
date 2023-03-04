from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.ZipCode)
admin.site.register(models.Settlement)
admin.site.register(models.FederalEntity)
admin.site.register(models.Municipality)


