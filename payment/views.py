from time import strftime
from urllib import response
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.contrib.sites.shortcuts import get_current_site

from django.views.decorators.csrf import csrf_exempt

from django.views.decorators.cache import cache_control


# ******************* MODELS AND VIEWS FROM OTHER APPS *************************
from account.models import CustomUser
import payment

from .models import ServiceProduct, UserSubscription

# ******************* MODELS AND VIEWS FROM OTHER APPS *************************

from django.contrib import messages

from datetime import datetime, timedelta

from django.http import HttpResponse, HttpResponseBadRequest

# ***************** FOR PAYMENTS ***********************
from django.conf import settings
import razorpay

# ****************** END FOR PAYMENTS *********************


def sub_selection(request):
        return render(request, 'payment/sub_selection.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def pay(request):
    
    if request.method == 'POST':

        try:
            cust_email = request.POST.get('email')

            duration = request.POST.get('duration')

            service = request.POST.get('category')

            subscribed_on = datetime.now()

            client = razorpay.Client(auth=(settings.RAZORPAY_ID , settings.RAZORPAY_ACCOUNT_ID))

            notes = {
                    'order-type': 'This is a subsciption order'
                    }

            callback_url = 'http://' + str(get_current_site(request))+"/payment/handlerequest"

            if cust_email is None or cust_email == "":

                messages.error(request, "Enter Your Registered Email First")
                return redirect('sub-selection')

            elif service is None or service == '0':
                messages.error(request, "Please choose a category")
                return redirect('sub-selection')
            elif duration is None or duration == '0':
                messages.error(request, "Please choose a duration of subscription")
                return redirect('sub-selection')       
            else:
                if CustomUser.objects.filter(email = cust_email).exists():     

                    user_instance = CustomUser.objects.get(email = cust_email)
                
                    if duration == '1':

                        expiry = subscribed_on + timedelta(days=30)


                        service_choosen = ServiceProduct.objects.get(code = service)

                        price = service_choosen.monthly_price * 100


                        if UserSubscription.objects.filter(user = user_instance,service_choosen = service_choosen, is_active = True, paid=True).exists():

                            messages.info(request, "This Subscription is already active.")
                            return redirect('sub-selection')
                        else:

                            if UserSubscription.objects.filter(user = user_instance,service_choosen = service_choosen, is_active = False, paid=False).exists():

                                del_sub_obj = UserSubscription.objects.get(user = user_instance,service_choosen = service_choosen)
                                del_sub_obj.delete()

                            subscription_obj = UserSubscription(user = user_instance, service_choosen = service_choosen, 
                            amount = price/100,subscription_duration = duration, subscribed_on = subscribed_on,expiring_on = expiry)
                            subscription_obj.save()

                            razorpay_order = client.order.create({
                            "amount": price,
                            "currency": "INR",
                            "notes": notes,
                            "receipt": subscription_obj.payment_id,
                            "payment_capture":'0',
                            })

                            order_status = razorpay_order['status']

                            if order_status  == 'created':
                            
                                subscription_obj.razorpay_order_id = razorpay_order['id']

                                subscription_obj.save()
                                context = {
                                    'order': str(service_choosen) + 'Q', 
                                    'order_id': razorpay_order['id'],
                                    'orderId': subscription_obj.razorpay_order_id,
                                    'price_summary': price/100,
                                    'price': price,
                                    'razorpay_merchant_id': settings.RAZORPAY_ID,
                                    'callback_url': callback_url,
                                    'service': service_choosen,
                                    'duration':subscription_obj.get_subscription_duration_display(),
                                    "user_name":user_instance.full_name,
                                    "user_phone": user_instance.phone_no,
                                    "user_email":user_instance.email,

                                }

                                return render(request, 'payment/payment_summary.html', context)
                            else:
                                messages.error(request, "Due to some issues we are unable to process the payment request. Please try again after some time.")
                                return redirect('sub-selection')
                        
                    elif duration == '3':

                        expiry = subscribed_on + timedelta(days=90)


                        service_choosen = ServiceProduct.objects.get(code = service)

                        price = service_choosen.quaterly_price * 100

                        if UserSubscription.objects.filter(user = user_instance,service_choosen = service_choosen, is_active = True, paid = True).exists():

                            messages.info(request, "The Subscription is already active.")
                            return redirect('sub-selection')
                        else:
                            
                            if UserSubscription.objects.filter(user = user_instance,service_choosen = service_choosen, is_active = False, paid=False).exists():

                                del_sub_obj = UserSubscription.objects.get(user = user_instance,service_choosen = service_choosen)
                                del_sub_obj.delete()

                            subscription_obj = UserSubscription(user = user_instance, service_choosen = service_choosen, 
                            amount = price/100,subscription_duration = duration, subscribed_on = subscribed_on,expiring_on = expiry)
                            subscription_obj.save()

                            razorpay_order = client.order.create({
                            "amount": price,
                            "currency": "INR",
                            "notes": notes,
                            "receipt": subscription_obj.payment_id,
                            "payment_capture":'0',
                            })


                            order_status = razorpay_order['status']

                            if order_status  == 'created':
                            
                                subscription_obj.razorpay_order_id = razorpay_order['id']

                                subscription_obj.save()
                                context = {
                                    'order': str(service_choosen) + 'M', 
                                    'order_id': razorpay_order['id'],
                                    'orderId': subscription_obj.razorpay_order_id,
                                    'price_summary': price/100,
                                    'price': price,
                                    'razorpay_merchant_id': settings.RAZORPAY_ID,
                                    'callback_url': callback_url,
                                    'service': service_choosen,
                                    'duration':subscription_obj.get_subscription_duration_display(),
                                    "user_name":user_instance.full_name,
                                    "user_phone": user_instance.phone_no,
                                    "user_email":user_instance.email,

                                }

                                return render(request, 'payment/payment_summary.html', context)
                            else:
                                messages.error(request, "Due to some issues we are unable to process the payment request. Please try again after some time.")
                                return redirect('sub-selection')

                    else:

                        expiry = subscribed_on + timedelta(days=180)


                        service_choosen = ServiceProduct.objects.get(code = service)
                        
                        price = service_choosen.hf_price * 100

                        if UserSubscription.objects.filter(user = user_instance,service_choosen = service_choosen, is_active = True, paid = True).exists():

                            messages.info(request, "The Subscription is already active.")
                            return redirect('sub-selection')
                        else:
                            if UserSubscription.objects.filter(user = user_instance,service_choosen = service_choosen, is_active = False, paid=False).exists():

                                del_sub_obj = UserSubscription.objects.get(user = user_instance,service_choosen = service_choosen)
                                del_sub_obj.delete()

                            subscription_obj = UserSubscription(user = user_instance, service_choosen = service_choosen, 
                            amount = price/100,subscription_duration = duration, subscribed_on = subscribed_on,expiring_on = expiry)
                            subscription_obj.save()

                            razorpay_order = client.order.create({
                            "amount": price,
                            "currency": "INR",
                            "notes": notes,
                            "receipt": subscription_obj.payment_id,
                            "payment_capture":'0',
                            })


                            order_status = razorpay_order['status']

                            if order_status  == 'created':
                            
                                subscription_obj.razorpay_order_id = razorpay_order['id']

                                subscription_obj.save()
                                context = {
                                    'order': str(service_choosen) + 'M', 
                                    'order_id': razorpay_order['id'],
                                    'orderId': subscription_obj.razorpay_order_id,
                                    'price_summary': price/100,
                                    'price': price,
                                    'razorpay_merchant_id': settings.RAZORPAY_ID,
                                    'callback_url': callback_url,
                                    'service': service_choosen,
                                    'duration':subscription_obj.get_subscription_duration_display(),
                                    "user_name":user_instance.full_name,
                                    "user_phone": user_instance.phone_no,
                                    "user_email":user_instance.email,

                                }

                                return render(request, 'payment/payment_summary.html', context)
                            
                else:

                    messages.warning(request, 'The user does not exist. Please register as Professional to opt for the subscription')
                    return redirect('sub-selection')
        
        except Exception as e:
            print(e)
            messages.error(request, "We are facing some problems. We regret the inconvinience caused.")
            return redirect('sub-selection')
    else:
        return HttpResponseBadRequest()

@csrf_exempt
def handlerequest(request):

    client = razorpay.Client(auth=(settings.RAZORPAY_ID , settings.RAZORPAY_ACCOUNT_ID))

    if request.method == 'POST':

        try:
            razorpay_payment_id = request.POST.get('razorpay_payment_id', '')
            order_id =  request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            params_dict={
                "razorpay_payment_id": razorpay_payment_id,
                "razorpay_order_id":  order_id,
                "razorpay_signature":  signature
                }
                
            try:
                sub_obj = UserSubscription.objects.get(razorpay_order_id = order_id)
            except:
                return HttpResponse('505 not found')

            sub_obj.razorpay_payment_id = razorpay_payment_id
            sub_obj.razorpay_signature = signature

            result = client.utility.verify_payment_signature(params_dict)
            
            if result == None:
                amount = sub_obj.amount*100
                client.payment.capture(razorpay_payment_id, amount)
                sub_obj.paid = True
                sub_obj.payment_status = 1
                sub_obj.is_active = True
                sub_obj.save()

                request.session['payment_id'] = sub_obj.payment_id
                return redirect('successful')
            else:
                sub_obj.delete()
                messages.error(request, "Your payment was unsuccesful. Please try re-subscribing.")
                return redirect('sub-selection')
        except Exception as e:
            print(e)
            messages.error(request,"We are facing some problems. If the payment is successful your subscription will automatically activated.")
            return redirect('sub-selection')

    else:
        return HttpResponseBadRequest()
def successpay(request):
    payment_id = request.session['payment_id']

    context = {
        'payment_id': payment_id
    }

    del request.session['payment_id']

    request.session.modified = True
    return render(request, 'payment/payment_successful.html', context)