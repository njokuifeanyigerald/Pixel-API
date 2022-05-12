# Pixel API

**Installation**
```xml
pip install pipenv
pipenv shell
```

```xml
pipenv install django djangorestframework pillow django-cors-headers djangorestframework-simplejwt
```

`to start the app`
```xml
django-admin startproject pixel ./

python manage.py startapp authentication
python manage.py startapp app
```

`for running TestCase`
```xml
pipenv install coverage 

coverage run manage.py test && coverage report && coverage html
```


`for swagger`
```xml
pipenv install  drf-yasg
```

## Description of project
The project about building a kinda Pixel or Image  API that allows any user to upload an image in PNG or JPG format.

**In The Authentication Section**
- In the models.py, I added a plan whereby a user can choose different plan ranging from `"Basic"`, `"Premium"` or `"Enterprise"`
- I implementated the registeration and login models and routes(even though I had to skip it), I did it so any user can register and login, then upload data to the API without having to go through the admin section to do it
- added logout ability to the API.

**In The App Section**
- In the app section, I Created a Route for an authentication user can upload an image and can get it according to the plan,  there are three bultin account tiers or plan: `Basic, Premium and Enterprise` for an authenticated user: Route address  - `http://127.0.0.1:8000/image/`
    **users that have "Basic" plan after uploading an image get:** 
        to a thumbnail that's 200px in height
    **users that have "Premium" plan get:**
        a link to a thumbnail that's 200px in height
        a link to a thumbnail that's 400px in height
        a link to the originally uploaded image
    **users that have "Enterprise" plan get**
        a link to a thumbnail that's 200px in height
        a link to a thumbnail that's 400px in height
        a link` to the originally uploaded image

- There is a route whereby users can change their plan or tier based on their subscription.
    Route address  - `http://127.0.0.1:8000/image/plan/`

-  I created a route for any one(unathenticated user) that visits the API to view images.
    Route address  - `http://127.0.0.1:8000/image/all/`
    
   


