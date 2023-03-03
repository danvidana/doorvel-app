from django.db import models

class ZipCode(models.Model):
  zip_code = models.CharField(max_length=5, primary_key=True)
  locality = models.CharField(max_length=120)
  
class federal_entity(models.Model):
  key = models.ForeignKey(ZipCode, on_delete=models.CASCADE)
  name = models.CharField(max_length=120)
  code = None