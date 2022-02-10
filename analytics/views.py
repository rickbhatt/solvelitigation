from django.shortcuts import render

from datetime import datetime

from . models import VisitorCount

def get_ip(request):

    try:
        ip_forward = request.META.get('HTTP_X_FORWARDED_FOR')
        if ip_forward:
            ip = ip_forward.split(",")[0]
            print("returning forwarded for ip address", ip)

        elif request.META.get('HTTP_X_REAL_IP'):
            ip = request.META.get('HTTP_X_REAL_IP')
            print ("returning REAL_IP ", ip)

        else:
            ip = request.META.get('REMOTE_ADDR')
            print("returning remote address ", ip)

    except:
        ip= ""
    
    return ip

def visitor_count(ip):

    visitor = VisitorCount()

    visitor.ip = ip
    visitor.date_of_record = datetime.now()

    if VisitorCount.objects.all().filter(ip = visitor.ip ,date_of_record__icontains= datetime.today().date()).exists():
        pass
        print("\n the ip", visitor.ip,"recorded on", visitor.date_of_record ,"already exists and wil not be saved \n")
    else:
        print('\n this is the ip address of the user that has been saved', visitor.ip, "\n")

        visitor.save()
    return print('the function is executed')
