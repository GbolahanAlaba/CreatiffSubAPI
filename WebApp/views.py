from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Creating API endpoint
@api_view(['GET', 'POST', 'Delete'])
def Subscribers(request):

    # get all the subscriptions
    # serialize them
    # return json
    if request.method == 'GET':
        sub = Subscriptions.objects.all()
        serializer = SubSerializer(sub, many=True)
        return Response(serializer.data)
        
    elif request.method == 'POST':
        serializer = SubSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.validated_data.get("Email",None)
            is_exist = Subscriptions.objects.filter(Email=email).exists()
            if is_exist:
                return Response({"error":"User with email already exist"},status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer.save()
                return Response(serializer.data, status.HTTP_201_CREATED)
        
        else:
            return Response({"Invalid Details"}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"Invalid Request"}, status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['GET', 'PUT', 'DELETE'])
def SubscribeDetail(request, id):
    try:
       sub = Subscriptions.objects.get(pk=id)
    except Subscriptions.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SubSerializer(sub)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SubSerializer(sub, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        sub.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


        
    
# Create your views here.
