import json
from multiprocessing import context
from django.http import JsonResponse
from django.shortcuts import render
import requests
from .models import ImageModel
from rest_framework.views import APIView
from rest_framework import status, response, permissions
from .serializer import ImageSerializer, Image200pxSerializer,ImageAnyoneSerializer


class ImageAPI(APIView):
    serializer_200_class = Image200pxSerializer
    serializer_class = ImageSerializer

    def get(self, request):
        user=request.user
        if user.plan == 'Basic':
            imagedata=  ImageModel.objects.all()
            serializer = Image200pxSerializer(imagedata, many=True)

            
            return response.Response({'image':serializer.data}, status=status.HTTP_200_OK)

        if user.plan == 'Premium':
            imagedata=  ImageModel.objects.all()
            serializer = self.serializer_class(imagedata, many=True)

            
            return response.Response({'image':serializer.data}, status=status.HTTP_200_OK)
        if user.plan == 'Enterprise':
            imagedata=  ImageModel.objects.all()
            
            serializer = self.serializer_class(imagedata, many=True)

            
            return response.Response({'image':serializer.data}, status=status.HTTP_200_OK)
        return response.Response()

        
    def post(self, request,  format=None):
        data = request.data
        user = request.user


        title = data['title']
        image = data['image']
        if  user.plan == 'Premium':
            imageData =  ImageModel.objects.create(user=user,title=title,image=image)
            serializer = self.serializer_class(imageData)
            context  = {
                'serializer':  serializer.data
            }
            return response.Response(context,status.HTTP_201_CREATED)

        if  user.plan == 'Enterprise':
            imageData =  ImageModel.objects.create(user=user,title=title,image=image)
            serializer = self.serializer_class(imageData)
            context  = {
                'serializer':  serializer.data
            }
            return response.Response(context,status.HTTP_201_CREATED)

        imageData =  ImageModel.objects.create(
            user= user,
            title =title,
            image = image
        )
        serializer = self.serializer_200_class(imageData)
        context  = {
            'serializer':  serializer.data
        }
        return response.Response(context,status.HTTP_201_CREATED)
    

class ImageAPIAnyone(APIView):
    def get(self, request):
        imagedata=  ImageModel.objects.all()
        serializer = ImageAnyoneSerializer(imagedata, many=True)
        return response.Response({'image':serializer.data}, status=status.HTTP_200_OK)