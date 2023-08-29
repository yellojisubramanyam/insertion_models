from django.shortcuts import render

# Create your views here.
from app.models import *
from django.http import HttpResponse
from django.db.models import Q

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

#create from views

def display_topics(request):
    qsto=topic.objects.all()
    qsto=topic.objects.exclude(topic_name='cricket')
    qsto=topic.objects.all()[0:4:1]


    d={'qsto':qsto}
    return render(request,'display_topics.html',d)

def display_webpage(request):
    QSWO = webpage.objects.filter(pk=3)
    QSWO = webpage.objects.filter(topic_name='cricket')
    QSWO = webpage.objects.all()

    # lookups ----> startswith .
    QSWO = webpage.objects.filter(name__startswith='v')

    # lookups ----> endswith .
    QSWO = webpage.objects.filter(url__endswith='in')

    # lookups ----> contains
    QSWO = webpage.objects.filter(url__contains='k')

     # using and----->(&)operator
    QSWO=webpage.objects.all()
    QSWO=webpage.objects.filter(Q(name__startswith='r') & Q(url__endswith='in'))

     # using or----->(|) operator 
    QSWO=webpage.objects.all()
    QSWO=webpage.objects.filter(Q(name__startswith='r') | Q(url__endswith='in'))




    d={'QSWO':QSWO}
    return render(request,'display_webpage.html',d)

 



def access_record1(request):
    qsao=access_record.objects.all()



    d={'qsao':qsao}
    return render(request,'access_record1.html',d)







def insert_topic(request):
    tn=input('enter topic_name: ')
    to=topic.objects.get(topic_name=tn)
    to.save()
    qsto=topic.objects.all()
    d={'qsto':qsto}
    return render(request,'display_topics.html',d)

def insert_webpage(request):
    tn=input('enter topic_name: ')
    na=input('enter name: ')
    ur=input('enter url: ')
    to=topic.objects.get(topic_name=tn)
    wo=webpage.objects.get_or_create(topic_name=to,name=na,url=ur)[0]
    wo.save()
    qswo=webpage.objects.all()
    d={'qswo':qswo}
    return render(request,'display_webpage.html',d)

def insert_accessrecord(request):
    name=input('enter name: ')
    date=input('enter date: ')
    author=input('enter author: ')
    wo=webpage.objects.get(name=name)
    ao=access_record.objects.get_or_create(name=wo,date=date,author=author)[0]
    ao.save()
    qsao=access_record.objects.all()
    d={'qsao':qsao}
    return render(request,'access_record1.html',d)











