from django.db import models

# Create your models here.
class Gallery(models.Model):
    Event_Name=models.TextField()
    Image1= models.ImageField(upload_to='pics')
    Image2= models.ImageField(upload_to='pics')
    Image3= models.ImageField(upload_to='pics')
    Image4= models.ImageField(upload_to='pics')
    Image5= models.ImageField(upload_to='pics')
    Image6= models.ImageField(upload_to='pics')
    Image7= models.ImageField(upload_to='pics')
    Image8= models.ImageField(upload_to='pics')
    Image9= models.ImageField(upload_to='pics')
    Image10= models.ImageField(upload_to='pics')
    Image11= models.ImageField(upload_to='pics')
    Image12= models.ImageField(upload_to='pics')
    Image13= models.ImageField(upload_to='pics')
    Image14= models.ImageField(upload_to='pics')
    Image15= models.ImageField(upload_to='pics')
    Image16= models.ImageField(upload_to='pics')
    Image17= models.ImageField(upload_to='pics')
    Image18= models.ImageField(upload_to='pics')
    Image19= models.ImageField(upload_to='pics')
    Image20= models.ImageField(upload_to='pics')
    Image21= models.ImageField(upload_to='pics')
    Image22= models.ImageField(upload_to='pics')
    Image23= models.ImageField(upload_to='pics')
    Image24= models.ImageField(upload_to='pics')
    Image25= models.ImageField(upload_to='pics')


class Courses(models.Model):
    Course_title=models.TextField()
    # description about course
    Desc=models.TextField()

class Teachers(models.Model):
    Teacher_name=models.TextField()
    description_of_teacher=models.TextField()
    photo=models.ImageField(upload_to='pics',null='true')
    Education=models.TextField()
