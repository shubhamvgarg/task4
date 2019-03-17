from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json
from django.http import HttpRequest
from MediaApi.models import Images
from MediaApi.serializers import ImageSerializer

# Create your views here.

@api_view(["GET"])
def GetAll(request):
    try:
        serializer = ImageSerializer(Images.objects.all(), many=True)
        return Response(serializer.data)
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)

@api_view(["GET","DELETE"])
def GetOne(request,id):
    if request.method=='GET':
        try:
            serializer = ImageSerializer(Images.objects.filter(id=id),many=True)
            return Response(serializer.data)
        except ValueError as e:
            return Response(e.args[0],status.HTTP_400_BAD_REQUEST)
    if request.method=='DELETE':
        try:
            Images.objects.filter(id=id).delete()
            return Response("Removed Successfully")
        except ValueError as e:
            return Response(e.args[0],status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def GetByUser(request,creater):

    try:
        serializer = ImageSerializer(Images.objects.filter(createdby=creater), many=True)
        return Response(serializer.data)
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def AddImage(request):
    file_serializer = ImageSerializer(data=request.data)
    if file_serializer.is_valid():
        file_serializer.save()
        return Response(file_serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["PUT"])
def UpdateImage(request):
    ins=Images.objects.get(name=request.data["name"])
    file_serializer = ImageSerializer(ins,data=request.data, partial=True)
    if file_serializer.is_valid():
        file_serializer.save()
        return Response(file_serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
