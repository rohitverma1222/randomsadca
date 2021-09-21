
from django.shortcuts import render
from .models import Gallery
from .models import Courses
from .models import Teachers
from django.core.mail import send_mail
# Create your views here.
def home(request):
    # gal=Gallery.objects.all()
    return render(request,'university/index.html')
def about(request):
    return render(request,'university/about.html')

def course(request):
    cou=Courses.objects.all()
    teach=Teachers.objects.all()
    return render(request,'university/course.html',{'cou':cou,'teach':teach})

def gallery(request):
    gal=Gallery.objects.all()

    return render(request,'university/gallery.html',{'gal':gal})

def contact(request):
    if request.method=='POST':
        name=request.POST.get('yourName')

        phone_no=str(request.POST.get('phone'))
        email_id=request.POST.get('email')
        course=request.POST.get('subject')
        Message=request.POST.get('Message')

        send_mail(
            phone_no,
            course,
            Message,
            ['rv432222@gmail.com'],
            fail_silently=False,
        )
        # print(name+phone_no+email_id+course+Message)
    return render(request,'university/contact.html')