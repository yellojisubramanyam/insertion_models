from django.shortcuts import render

# Create your views here.
from app.models import *
from django.http import HttpResponse

def insert_topic(request):
    tn=input('enter topicname: ')
    to=topic.objects.get_or_create(topic_name=tn)[0]
    to.save()
    return HttpResponse('data inserted successfully')
  

def insert_webpage(request):
    tn=input('enter topic_name: ')
    to=topic.objects.get_or_create(topic_name=tn)[0]
    to.save()
    n=input('enter name: ')
    u=input('enter url: ')
    wo=webpage.objects.get_or_create(topic_name=to,name=n,url=u)[0]
    wo.save()
    return HttpResponse('data inserted successfully')

def insert_ac(request):
    tn=input('enter topic_name: ')
    to=topic.objects.get_or_create(topic_name=tn)[0]
    to.save()
    n=input('enter name: ')
    u=input('enter url: ')
    wo=webpage.objects.get_or_create(topic_name=to,name=n,url=u)[0]
    wo.save()
    d=input('enter date: ')
    a=input('enter author: ')
    e=input('enter email: ')
    ao=access_record.objects.get_or_create(name=wo,date=d,author=a)[0]
    ao.save()
    return HttpResponse('data inserted successfully')