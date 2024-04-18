from rest_framework.response import Response
from rest_framework.views import APIView
from project.serializer.celular_serializer import CelularSerializers
from api.models.celular import Celular
from rest_framework import status
from django.http import Http404


class Celular_APIView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        celular = Celular.objects.all()
        serializer = CelularSerializers(celular, many=True)
        
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = CelularSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class Celular_APIView_Detail(APIView):
    def get_object(self, pk):
        try:
            return Celular.objects.get(pk=pk)
        except Celular.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        celular = self.get_object(pk)
        serializer = CelularSerializers(celular)  
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        celular = self.get_object(pk)
        serializer = CelularSerializers(celular, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        celular = self.get_object(pk)
        celular.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)