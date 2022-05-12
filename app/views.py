from .models import ImageModel
from rest_framework.views import APIView
from rest_framework import status, response, permissions
from .serializer import ImageSerializer, Image200pxSerializer,ImageAnyoneSerializer

from authentication.models import User


# API FOR ONLY AUTHENTICATED USERS
class ImageAPI(APIView):
    # SERIALIZER CLASS FOR BASIC PLAN
    serializer_200_class = Image200pxSerializer
    # SERIALIZER CLASS FOR PREMIUM AND ENTERPRISE PLAN
    serializer_class = ImageSerializer

    def get(self, request):
        user=request.user
        if user.is_authenticated:
            if user.plan == 'Basic':
                imagedata=  ImageModel.objects.all()
                serializer = Image200pxSerializer(imagedata, many=True)

                
                return response.Response({'image':serializer.data}, status=status.HTTP_200_OK)

            elif user.plan == 'Premium':
                imagedata=  ImageModel.objects.all()
                serializer = self.serializer_class(imagedata, many=True)

                
                return response.Response({'image':serializer.data}, status=status.HTTP_200_OK)
            elif user.plan == 'Enterprise':
                imagedata=  ImageModel.objects.all()
                
                serializer = self.serializer_class(imagedata, many=True)

                
                return response.Response({'image':serializer.data}, status=status.HTTP_200_OK)

        else:
            return response.Response({'error': 'pls authenticate user'}, status.HTTP_401_UNAUTHORIZED)

        
    def post(self, request,  format=None):
        
        # try:
        data = request.data
        user = request.user


        title = data['title']
        # tried doing validation in serializer.py but it wasn't working out 
        # was confused so I decided to go old school by doing it in views.py
        if title == '':
            return  response.Response({'error': 'title must not be blank'}, status.HTTP_400_BAD_REQUEST)
        image = data['image']
        if user.is_authenticated:
            if  user.plan == 'Premium':
                imageData =  ImageModel.objects.create(user=user,title=title,image=image)
                serializer = self.serializer_class(imageData)
                context  = {
                    'serializer':  serializer.data
                }
                return response.Response(context,status.HTTP_201_CREATED)

            elif  user.plan == 'Enterprise':
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
            serializer = Image200pxSerializer(imageData)
            context  = {
                'serializer':  serializer.data
            }
            return response.Response(context,status.HTTP_201_CREATED)
        else:
            return response.Response({'error': 'pls authenticate user'}, status.HTTP_401_UNAUTHORIZED)
        

class ChangePlan(APIView):
    def post(self, request, format=None):
        user = request.user
        data = request.data
        if user.is_authenticated:
            plan = data['plan']
            if plan == '':
                return  response.Response({'error': 'pls choose a plan'}, status.HTTP_400_BAD_REQUEST)
            User.objects.filter(email=user.email).update(
                plan=plan
            )  
            return response.Response({'success':'plan successfully changed'},
                            status=status.HTTP_200_OK)      
        else:
             return response.Response({'error':' user is not authenticated '},
                            status=status.HTTP_401_UNAUTHORIZED)

    

class ImageAPIAnyone(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request):
        imagedata=  ImageModel.objects.all()
        serializer = ImageAnyoneSerializer(imagedata, many=True)
        return response.Response({'image':serializer.data}, status=status.HTTP_200_OK)