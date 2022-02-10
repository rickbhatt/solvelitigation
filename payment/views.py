from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# ******************* MODELS AND VIEWS FROM OTHER APPS *************************
from account.models import CustomUser

from .models import ServiceProduct, UserSubscription

# ******************* MODELS AND VIEWS FROM OTHER APPS *************************

from django.contrib import messages

from datetime import datetime, timedelta

from django.http import HttpResponse


def sub_selection(request):

    if request.method == 'POST':

        try:
            cust_email = request.POST.get('email')

            duration = request.POST.get('duration')

            service = request.POST.get('category')

            subscribed_on = datetime.now()

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
                
                    if duration == 'monthly':

                        expiry = subscribed_on + timedelta(days=30)


                        service_choosen = ServiceProduct.objects.get(code = service)

                        price = service_choosen.monthly_price * 100

                        if UserSubscription.objects.filter(user = user_instance,service_choosen = service_choosen, is_active = True).exists():

                            messages.info(request, "The Subscription is already active.")
                            return redirect('sub-selection')
                        else:

                            subscription_obj = UserSubscription(user = user_instance, service_choosen = service_choosen, subscribed_on = subscribed_on, expiring_on = expiry, is_active = True)
                            subscription_obj.save()

                            messages.info(request, "the payement was successful")
                            return redirect('sub-selection')
                        
                    elif duration == 'quaterly':

                        expiry = subscribed_on + timedelta(days=90)


                        service_choosen = ServiceProduct.objects.get(code = service)

                        price = service_choosen.quaterly_price * 100

                        if UserSubscription.objects.filter(user = user_instance,service_choosen = service_choosen, is_active = True).exists():

                            messages.info(request, "The Subscription is already active.")
                            return redirect('sub-selection')
                        else:
                            subscription_obj = UserSubscription(user = user_instance, service_choosen = service_choosen, subscribed_on = subscribed_on, expiring_on = expiry, is_active = True)
                            subscription_obj.save()

                            messages.info(request, "the payement was successful")
                            return redirect('sub-selection')

                    else:

                        expiry = subscribed_on + timedelta(days=180)


                        service_choosen = ServiceProduct.objects.get(code = service)
                        
                        price = service_choosen.hf_price * 100

                        if UserSubscription.objects.filter(user = user_instance,service_choosen = service_choosen, is_active = True).exists():

                            messages.info(request, "The Subscription is already active.")
                            return redirect('sub-selection')
                        else:
                            subscription_obj = UserSubscription(user = user_instance, service_choosen = service_choosen, subscribed_on = subscribed_on, expiring_on = expiry, is_active = True)
                            subscription_obj.save()

                            messages.info(request, "the payement was successful")
                            return redirect('sub-selection')
                            
                else:

                    messages.info(request, 'The user does not exist. Please register as Professional to opt for the subscription')
                    return redirect('sub-selection')
        
        except Exception as e:
            print(e)
            messages.error(request, "We are facing some problems. We regret the inconvinience caused.")
            return redirect('sub-selection')
    else:
        return render(request, 'payment/sub_selection.html')


@login_required(login_url='login')
def personal(request):

    subuser = request.user

    sub = UserSubscription.objects.filter(user = subuser, is_active = True)

    print('\n',subuser)
        
    for cust in sub:
        
        if cust.service_choosen.code == 11:
            print('Civil available')
        if cust.service_choosen.code == 21:
            print('Coorprate available')

        if cust.service_choosen.code == 31:
            print('Criminal available')

        if cust.service_choosen.code == 41:
            print('Service available')

        if cust.service_choosen.code == 51:
            print('Taxation available')
      
     

    return render(request, 'testpage.html', {'subuser': subuser, 'sub': sub})