from rest_framework import serializers
from .models import *

class ZipCodeSerializer(serializers.ModelSerializer):
  class Meta:
    model = ZipCode
    fields = [
      'zip_code',
      'locality',
    ]
    
class FederalEntitySerializer(serializers.ModelSerializer):
  class Meta:
    model = FederalEntity
    fields = [
      'key',
      'name',
      'code'
    ]
    
class MunicipalitySerializer(serializers.ModelSerializer):
  key = serializers.IntegerField(source='local_key')
  class Meta:
    model = Municipality
    fields = [
      'key',
      'name'
    ]
 
class SettlementSerializer(serializers.ModelSerializer):
  class Meta:
    model = Settlement
    fields = [
      'key',
      'name',
      'zone_type',
      'settlement_type',
      'settlement_local_key'
    ]