from django.db import models

class FederalEntity(models.Model):
  key = models.IntegerField(primary_key=True)
  name = models.CharField(max_length=120)
  code = models.CharField(max_length=120, blank=True, null=True)
  
  def __str__(self):
      return self.name

class Municipality(models.Model):
  key = models.CharField(max_length=120, primary_key=True)
  local_key = models.IntegerField()
  name = models.CharField(max_length=120)
  
  def __str__(self):
      return self.name
  
class ZipCode(models.Model):
  zip_code = models.CharField(max_length=5, primary_key=True)
  locality = models.CharField(max_length=120)
  federal_entity_fk = models.ForeignKey(FederalEntity, on_delete=models.CASCADE, blank=True, null=True)
  municipality_fk = models.ForeignKey(Municipality, on_delete=models.CASCADE, blank=True, null=True)
  
  def __str__(self):
      return self.zip_code

class Settlement(models.Model):
  key = models.CharField(max_length=120, primary_key=True)
  settlement_local_key = models.IntegerField()
  name = models.CharField(max_length=120)
  zone_type = models.CharField(max_length=120)
  settlement_type = models.CharField(max_length=120)
  zip_code_fk = models.ForeignKey(ZipCode, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.name