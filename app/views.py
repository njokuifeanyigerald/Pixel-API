import json
from multiprocessing import context
from django.http import JsonResponse
from django.shortcuts import render
import requests
from .models import ImageModel
from rest_framework.views import APIView
from rest_framework import status, response, permissions
from .serializer import ImageSerializer, Image200pxSerializer


class ImageAPI(APIView):
    serializer_class = ImageSerializer

    def get(self, request):
        user=request.user
        if user.plan == 'Basic':
            imagedata=  ImageModel.objects.all()
            serializer = Image200pxSerializer(imagedata, many=True)

            
            return response.Response({'image':serializer.data}, status=status.HTTP_200_OK)

        if user.plan == 'Premium':
            imagedata=  ImageModel.objects.all()
            serializer = ImageSerializer(imagedata, many=True)

            
            return response.Response({'image':serializer.data}, status=status.HTTP_200_OK)
        if user.plan == 'Enterprise':
            imagedata=  ImageModel.objects.all()
            
            serializer = ImageSerializer(imagedata, many=True)

            
            return response.Response({'image':serializer.data}, status=status.HTTP_200_OK)
        return response.Response()

        
    def post(self, request,  format=None):
        data = request.data
        user = request.user


        title = data['title']
        image = data['image']

        imageData =  ImageModel.objects.create(
            user= user,
            title =title,
            image = image
        )
        serializer = self.serializer_class(imageData)
        context  = {
            'serializer':  serializer.data
        }
        return response.Response(context,status.HTTP_201_CREATED)
    