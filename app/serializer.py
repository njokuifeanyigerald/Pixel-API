from attr import fields
from rest_framework import serializers
from .models import ImageModel

class ImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
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
    def get_image_url(self, obj):
        return obj.image.url
    def get_image_200px_url(self, obj):
        return obj.image_200px.url
    def get_image_400px_url(self, obj):
        return obj.image_400px.url

class Image200pxSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)
    image_200px = serializers.ImageField(required=False,  max_length=None, use_url=True)
    image_url = serializers.SerializerMethodField('get_image_url')
    image_200px_url = serializers.SerializerMethodField('get_image_200_url')
    
    class Meta:
        model = ImageModel
        fields = [
            'id','title', 'image', 'image_200px', 'user','image_url',
            'image_200px_url'
        ]
        read_only_fields = ['user']
    def get_image_url(self, obj):
        return obj.image.url
    def get_image_200_url(self, obj):
        return obj.image_200px.url

class ImageAnyoneSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)
    image_url = serializers.SerializerMethodField('get_image_url')
    
    class Meta:
        model = ImageModel
        fields = [
            'id','title', 'image', 'image_url'
        ]
        read_only_fields = ['user', 'image_url']
    def get_image_url(self, obj):
        return obj.image.url