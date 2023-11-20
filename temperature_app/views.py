from django.shortcuts import render
from .models import TemperatureReading
from .serializer import TemperatureSerializer
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# def temperatures(request):
#     TemperatureReading.objects.create(temperature=72.5, location='San Francisco')

#     readings = [
#     TemperatureReading(temperature=61.2, location='New York'),
#     TemperatureReading(temperature=58.7, location='Seattle'),
#     ]   
#     TemperatureReading.objects.bulk_create(readings)


#     print(TemperatureReading.objects.all())

#     return JsonResponse("Hello", safe=False)


class TemperatureVals(APIView):
    def get(self, request):
        temperatures = TemperatureReading.objects.all()
        serializer = TemperatureSerializer(temperatures, many=True)
        return Response(serializer.data)

class TempAdd(APIView):
    def post(self, request):
        serializer = TemperatureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class TempDetail(APIView):
    def get_temp_by_pk(self, pk):
        try:
            return TemperatureReading.objects.get(pk=pk)
        except:
            return Response({
                'error': 'Does not exist'
            }, status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request, pk):
        temp = self.get_temp_by_pk(pk)
        serializer = TemperatureSerializer(temp)
        return Response(serializer.data)
    
    def put(self, request, pk):
        temp = self.get_temp_by_pk(pk)
        serializer = TemperatureSerializer(temp, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        temp = self.get_temp_by_pk(pk)
        temp.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
# Create your views here.
