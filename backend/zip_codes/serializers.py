from rest_framework import serializers
from .models import *

class ZipCodeSerializer(serializers.ModelSerializer):
  locality = serializers.SerializerMethodField()
  class Meta:
    model = ZipCode
    fields = [
      'zip_code',
      'locality',
    ]
  def get_locality(self, obj):
        return obj.locality.upper() if obj.locality else None
  
class FederalEntitySerializer(serializers.ModelSerializer):
  name = serializers.SerializerMethodField()
  class Meta:
    model = FederalEntity
    fields = [
      'key',
      'name',
      'code'
    ]
  def get_name(self, obj):
        return obj.name.upper() if obj.name else None
    
class MunicipalitySerializer(serializers.ModelSerializer):
  key = serializers.IntegerField(source='local_key')
  name = serializers.SerializerMethodField()
  class Meta:
    model = Municipality
    fields = [
      'key',
      'name'
    ]
  def get_name(self, obj):
        return obj.name.upper() if obj.name else None
 
class SettlementSerializer(serializers.ModelSerializer):
  key = serializers.IntegerField(source='settlement_local_key')
  name = serializers.SerializerMethodField()
  class Meta:
    model = Settlement
    fields = [
      'key',
      'name',
      'zone_type',
      'settlement_type',
    ]
  def get_name(self, obj):
        return obj.name.upper() if obj.name else None