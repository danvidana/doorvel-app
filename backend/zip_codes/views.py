from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
import json

from .models import *
from .serializers import *

@api_view(["GET"])
def zipCode_home(request, *args, **kwargs):
  """
  ZipCode Home View
  """
  return Response({"view": "ZipCode Home view"})

@api_view(["GET"])
def zipCode_id(request, zip_code_arg, *args, **kwargs):
  """
  ZipCode Resource Agrument View
  """
  zipCodeInstance = ZipCode.objects.get(zip_code=zip_code_arg)
  settlementsInstance = Settlement.objects.filter(zip_code_fk=zip_code_arg)
  federalEntityInstance = zipCodeInstance.federal_entity_fk
  municipalityInstance = zipCodeInstance.municipality_fk
  
  if zipCodeInstance:
    data = {}
    data.update(ZipCodeSerializer(zipCodeInstance).data)
    data["federal_entity"] = FederalEntitySerializer(federalEntityInstance).data
    data["settlements"] = []
    for settlement in settlementsInstance:
      data["settlements"].append(SettlementSerializer(settlement).data)
    for settlement in data["settlements"]:
      string = settlement["settlement_type"]
      settlement["settlement_type"] = {"name": string}
    data["municipality"] = MunicipalitySerializer(municipalityInstance).data
  return JsonResponse(data)