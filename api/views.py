from django.http import HttpResponse
from django.shortcuts import render
import io
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from requests import request
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework import serializers

from api.serializers import StudentSerializer
# Create your views here.


@method_decorator(csrf_exempt, name='dispatch')
class StudentApi(View):
    def post(self,request):
        data = request.body
        data = io.BytesIO(data)
        data = JSONParser().parse(data)
        serializer= StudentSerializer(data =data)
        if serializer.is_valid():
            serializer.save()
            data = {'msg' : 'Data Saved Successfully'}
            data =JSONRenderer().render(data)
            return HttpResponse(data, content_type = 'application/json')
        else:
            data = {'msg' : 'Please Enter Valid Data'}
            data = JSONRenderer().render(data)
            return HttpResponse(data, content_type='application/json')
    def get(self, request):
        return HttpResponse("hi")