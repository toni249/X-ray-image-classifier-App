from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Patient_info
from django.contrib import messages
from django.conf import settings

import tensorflow as tf
import numpy as np

from django.core.mail import send_mail


# Create your views here.

# def home (request):
#     return HttpResponse("we are in home now")


# def home (request):
#     return render(request,"home.html",{})
model = tf.keras.models.load_model('super_model.h5')

def image_pred(img):

    path = settings.MEDIA_ROOT + img
    img = tf.keras.preprocessing.image.load_img(path,color_mode='grayscale',target_size=(500,500))
    image_array = tf.keras.preprocessing.image.img_to_array(img)
    image_array = np.reshape(image_array , (500,500,1))
    image_array = tf.expand_dims(image_array,0)
    pred = model.predict(image_array)
    print("prediction = ",pred)
    return np.argmax(pred)

def newhome(request):
    if request.method=='POST':
        name = request.POST['name']
        mail = request.POST['mail']
        image = request.FILES['image']

        data = Patient_info(name = name , mail = mail, xray_sheet = image)
        data.save()

        result = image_pred(data.xray_sheet.name)
        
        if result==0:
            #send_mail('X-ray test result','You are infected with covid','imtony1304@gmail.com',mail,fail_silently=False,)
            return render(request,'covid.html')
        elif result==1:
            #send_mail('X-ray test result','You are a healthy person','imtony1304@gmail.com',mail,fail_silently=False,)
            return render (request,'normal.html')
        else:
            #send_mail('X-ray test result','You are infected with Pneumonia','imtony1304@gmail.com',mail,fail_silently=False,)
            return render (request,'pneumonia.html')

        # messages.success(request, 'Response has been recorded ')
        # return redirect('form')

        # return render(request, 'result.html',{'res':result})

    return render(request,'newhome.html')