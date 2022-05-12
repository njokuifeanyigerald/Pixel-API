from django.forms import ValidationError
from rest_framework import serializers
from .models import ImageModel
from django.conf import settings

# FOR PREMIUM OR ENTERPRISE USERS
class ImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required = True)
    image_200px = serializers.ImageField(required=False,  max_length=None, )
    image_400px = serializers.ImageField(required=False,  max_length=None)
    image_url = serializers.SerializerMethodField('get_image_url')
    image_200px_url = serializers.SerializerMethodField('get_image_200px_url')
    image_400px_url = serializers.SerializerMethodField('get_image_400px_url')

     
    
    class Meta:
        model = ImageModel
        fields = [
            'id','title', 'image', 'image_200px', 'image_400px', 'user', 
            'image_url', 'image_200px_url', 'image_400px_url'
        ]
        read_only_fields = ['user', 'image_200px', 'image_400px', 'image_200px_url', 'image_400px_url' ]

    
    # GETTING THE URL OF THE IMAGES FOR NORMAL SIZE
    def get_image_url(self, obj):
       return  "http://127.0.0.1:8000" + obj.image.url

    # GETTING THE URL OF THE IMAGES FOR 200PX SIZE
    def get_image_200px_url(self, obj):
        if obj.image_200px == "":
            return 'no url link'
        else:
            return  settings.HOST_URL + obj.image_200px.url
    # GETTING THE URL OF THE IMAGES FOR 400PX SIZE
    def get_image_400px_url(self, obj):
        if obj.image_400px == "":
            return 'no url 400px link for this file'
        else:
            return  settings.HOST_URL + obj.image_400px.url

    
        

# FOR BASIC PLAN  USERS
class Image200pxSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None,required = True, write_only=True)
    image_200px = serializers.ImageField(required=False,  max_length=None, use_url=True)
    image_200px_url = serializers.SerializerMethodField('get_image_200px_url')
    
    class Meta:
        model = ImageModel
        fields = [
            'id','title', 'image', 'image_200px', 'user',
            'image_200px_url'
        ]
        read_only_fields = ['user']

     # GETTING THE URL OF THE IMAGES
    def get_image_200px_url(self, obj):
        if obj.image_200px == "":
            return 'no url link'
        else:
            return settings.HOST_URL + obj.image_200px.url

    


# A SERIALIZER FOR ANY VIEWER OR VISITOR THAT AINT UNAUTHENTICATED YET
class ImageAnyoneSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)
    image_url = serializers.SerializerMethodField('get_image_url')
    
    class Meta:
        model = ImageModel
        fields = [
            'id','title', 'image', 'image_url'
        ]
        read_only_fields = ['user', 'image_url']

    # RETURN THE URL FOR IMAGE 
    def get_image_url(self, obj):
        return  settings.HOST_URL + obj.image.url