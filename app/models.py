from django.db import models
from django.forms import ValidationError
from authentication.models import User

from PIL import Image


from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys


class ImageModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    image = models.ImageField(upload_to='pics')
    image_200px = models.ImageField(upload_to='pics', blank=True, null=True)
    image_400px = models.ImageField(upload_to='pics', blank=True, null=True)

    

    def save(self, *args, **kwargs):
        # IF USER PLAN IS BASIC
        if self.user.plan == 'Basic':
            im = Image.open(self.image)
            print(im.format)

            output = BytesIO()

            #Resize/modify the image TO 200PX
            im = im.resize( (200,200) )

            #after modifications, save it to the output
            im.save(output, format='JPEG', quality=100)
            output.seek(0)

            #change the imagefield value to be the newley modifed image value
            self.image_200px = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.image.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)

        # IF USER PLAN IS PREMIUM
        if self.user.plan == 'Premium':
            im = Image.open(self.image)

            output = BytesIO()
            output400px = BytesIO()

            #Resize/modify the image TO 2OOPX
            im = im.resize( (200,200) )

            #Resize/modify the image TO 4OOPX
            im400px = im.resize((400,400))



            #after modifications, save it to the output FOR 200PX
            im.save(output, format='JPEG', quality=100)
            #after modifications, save it to the output FOR 200PX
            im400px.save(output400px, format='JPEG', quality=100)

            # 200PX
            output.seek(0)
            # 400PX
            output400px.seek(0)

            #change the imagefield value to be the newley modifed image value FOR 200PX
            self.image_200px = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.image.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)

            #change the imagefield value to be the newley modifed image value FOR 200PX
            self.image_400px = InMemoryUploadedFile(output400px,'ImageField', "%s.jpg" %self.image.name.split('.')[0], 'image/jpeg', sys.getsizeof(output400px), None)

        # IF USER PLAN IS ENTERPRISE
        if self.user.plan == 'Enterprise':
            im = Image.open(self.image)

            output = BytesIO()
            output400px = BytesIO()

            #Resize/modify the image TO 2OOPX
            im = im.resize( (200,200) )

            #Resize/modify the image TO 4OOPX
            im400px = im.resize((400,400))



            #after modifications, save it to the output FOR 200PX
            im.save(output, format='JPEG', quality=100)
            #after modifications, save it to the output FOR 200PX
            im400px.save(output400px, format='JPEG', quality=100)

            # 200PX
            output.seek(0)
            # 400PX
            output400px.seek(0)

            #change the imagefield value to be the newley modifed image value FOR 200PX
            self.image_200px = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.image.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)

            #change the imagefield value to be the newley modifed image value FOR 200PX
            self.image_400px = InMemoryUploadedFile(output400px,'ImageField', "%s.jpg" %self.image.name.split('.')[0], 'image/jpeg', sys.getsizeof(output400px), None)
        
        super(ImageModel,self).save()

    # RETURN DATA IN THE ADMIN
    def __str__(self):
        return self.title
