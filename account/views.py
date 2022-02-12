from django.shortcuts import render, redirect 

from django.contrib import messages

from django.contrib.auth import login, logout, authenticate

from django.views.decorators.cache import cache_control


from datetime import datetime

from django.http.response import HttpResponse

import uuid


##################### CUSTOM USER MODEL ###########################

from .models import CustomUser, ForgetPassword, UserOtp

#################### END OF CUSTOM USER MODEL ######################

##################### for otp ###########################

import random
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
##################### end for otp ###########################


#################### celery queing ############################

from .tasks import *

################# end of celery queing ######################

####################### OTHER APPS VIEWS AND MODELS ##################

from analytics.views import visitor_count, get_ip

####################### END OTHER APPS VIEWS AND MODELS ##################



def registerpage(request):

    if request.method == 'POST':
    
        try:
            
            get_otp = request.POST.get('otp')

            if get_otp:
                get_user= request.POST.get('user')
                user = CustomUser.objects.get(email=get_user)
            
                if int(get_otp) == UserOtp.objects.filter(user= user).last().otp:
                    user.is_active = True
                    user.save()
                    
                    # for celery
                    
                    name = user.full_name
                    user_email = user.email
                    regd_send_email.delay(name, user_email)

                
                    messages.success(request,'Your account has been created successfully.')
                    return redirect('login')
                else:
                    messages.error(request, 'OTP entered is wrong')
                    return render(request, 'account/register.html', {'otp': True, 'user': user})
            
            full_name = request.POST.get('full_name')
            age = request.POST.get('age')
            phone_no = request.POST.get('phone')
            state = request.POST.get('state')
            regd_as = request.POST.get('regd_as')
            email = request.POST.get('email')
            password1= request.POST.get('password')
            password2= request.POST.get('con_password')

            if password1==password2:
                if CustomUser.objects.filter(email=email).exists():
                    messages.info(request, 'User with same email already exists')
                    return redirect('register')
                elif int(age) < 18:
                        messages.info(request, 'You have to be above 18 to register')
                        return redirect('register')
                elif regd_as is None:
                        messages.info(request, 'Please select what you want to register as or register for')
                        return redirect('register')
                elif state is None:
                        messages.info(request, 'Please select a state/ ut')
                        return redirect('register') 
                else:
                    user=CustomUser.objects.create_user(full_name=full_name.upper(),age=age, phone_no=phone_no, state=state.upper(),  regd_as= regd_as,email=email.lower(), password=password1)
                    user.is_active = False
                    user.save()
  
                    usr_otp = random.randint(100000, 999999)
                    UserOtp.objects.create(user = user, otp = usr_otp)
                    
                    name= user.full_name
                    usr_otp = usr_otp
                    user_email = user.email
                    
                    otp_send_mail.delay(name, usr_otp, user_email)

                    
                    return render(request, 'account/register.html', {'otp': True, 'user': user})
            else:
                return redirect('register')
        
        except Exception as e:
        
            path = "account/views/registerpage()"

            date_of_record = datetime.now()

            error = str(e)
            
            send_to_developer.delay(path, date_of_record, error)
            print("\nthe exception is comming from regsiterpage : ", e, "\n")
            messages.error(request, 'We are facing some problem. We shall rectify it soon. Sorry for inconvenience caused.')
            return redirect('register')  

    else:
        return render(request, 'account/register.html')
    

def loginpage(request):
    
    if request.method == 'POST':
        
        get_otp = request.POST.get('otp')

        if get_otp:
            get_user= request.POST.get('user')
            user = CustomUser.objects.get(email=get_user)
           
            if int(get_otp) == UserOtp.objects.filter(user= user).last().otp:
                user.is_active = True
                user.save()
                
                # for celery
                
                name = user.full_name
                user_email = user.email

                regd_send_email.delay(name, user_email)

                
                login(request, user)
                return redirect('login')
            else:
                messages.error(request, 'OTP entered is wrong')
                return render(request, 'account/login.html', {'otp': True, 'user': user})
        
        
        # email=request.POST['email']               #this works too
        # password=request.POST['password']

        email =  request.POST.get('email')
        password = request.POST.get('password')

        # user = CustomUser.objects.get(email=username, password=password)
        

        user = authenticate(request, email= email, password= password) #changed username to email because Custom User has no username field

        if user is not None:
            
            if user.is_staff:
                login(request, user)
                return redirect('test-login') # this is in control views
            
            elif user.regd_as == 'professional':
                login(request, user)
                return redirect('professional-home')

            else:
                login(request, user)
                return redirect('test-login') # this is in home views
        
        elif not CustomUser.objects.filter(email=email).exists():
            messages.info(request, "No user with this username exists \n You are requested to register first.")
            return render( request, 'account/login.html')
        elif not CustomUser.objects.get(email=email).is_active:
            user = CustomUser.objects.get(email=email)

            usr_otp = random.randint(100000, 999999)
            UserOtp.objects.create(user = user, otp = usr_otp)
            
            name= user.full_name
            usr_otp = usr_otp
            user_email = user.email
                
            otp_send_mail.delay(name, usr_otp, user_email)
            return render(request, 'account/login.html', {'otp': True, 'user': user})
        
        else:
            messages.warning(request, 'UserID or Password is incorrect!')
            return render( request, 'account/login.html')            #FOR ERROR PURPOSE

    else:

        ip = get_ip(request)
        visitor_count(ip)

        return render(request, 'account/login.html')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logoutUser(request):                                    # FOR LOGOUT
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    else:
        logout(request)
        return redirect('home')



################## RESEND OTP ##################

def resend_otp(request):
    if request.method == 'GET':
        get_usr = request.GET['usr']
        
        if CustomUser.objects.filter(email=get_usr).exists() and not CustomUser.objects.get(email=get_usr).is_active:
            
                usr = CustomUser.objects.get(email=get_usr)
                
                usr_otp = random.randint(100000, 999999)
                UserOtp.objects.create(user = usr, otp = usr_otp)
                mess = f"Hello, {usr.full_name},\n Please enter the otp to validate your email and activate your account. \nYour OTP is {usr_otp} .\n Thanks!"
                
                send_mail(
                        "Welcome to Solve Litigation - Verify your Email",   #subject
                        mess,  #message
                        settings.EMAIL_HOST_USER,  # sender
                        [usr.email],           #reciever
                        fail_silently= False
                    )
                return HttpResponse("Resend")

    
    return HttpResponse("Can't Send OTP")

################## END OF RESEND OTP ############

#################### PASSWORD RESET CHANGE ######################

def change_password(request, token):

    try:
        fp_obj = ForgetPassword.objects.filter(forget_password_token = token).first()

        print("\nthis is user obj ", fp_obj.user, "\n")

        if request.method == 'POST':
            new_password = request.POST.get('password')
            con_password = request.POST.get('con_password')
            user_id = request.POST.get('user')

            if user_id is None:
                messages.error(request, 'User does not exist.')
                return redirect(request.path_info)
            else:
                if new_password != con_password:
                    messages.info(request, 'Password and Confirm Password not matching')
                    return redirect(request.path_info)
                else:
                    user_obj = CustomUser.objects.get(email = user_id)
                    user_obj.set_password(new_password)
                    user_obj.save()

                    messages.success(request, 'Password changed successfuly')

                    return redirect('login')


        context = {'user': fp_obj.user}

    except Exception as e:

        path = "account/views/change_password()"

        date_of_record = datetime.now()

        error = str(e)
        
        send_to_developer.delay(path, date_of_record, error)
        print("\nthe exception is comming from forget_password : ", e, "\n")
        messages.error(request, 'We are facing some problem. We shall rectify it soon. Sorry for inconvenience caused.')

        print("this is the exception from chamge_password : ", e)
        return redirect(request.path_info)

    return render(request, 'account/change_password.html', context)

def forget_password(request):

    try:

        if request.method == 'POST':
            user_email = request.POST.get('email')

            if CustomUser.objects.filter(email = user_email).exists():
                
                user_obj = CustomUser.objects.get(email = user_email)

                name = user_obj.full_name

                print("\n this is the user : ", user_obj, " this is its name : ", name,"\n")

                token = str(uuid.uuid4())
                
                fp = ForgetPassword.objects.get_or_create(user = user_obj, forget_password_token = token)

                forget_password_mail.delay(user_email, name, token)
                messages.info(request, f'An email has been sent to {user_obj}.')
                return redirect('forget-password')  
            else:
                messages.error(request, 'User does not exist')
                return redirect('forget-password')   

    except Exception as e:

        path = "account/views/forget_password()"

        date_of_record = datetime.now()

        error = str(e)
        
        send_to_developer.delay(path, date_of_record, error)
        print("\nthe exception is comming from forget_password : ", e, "\n")
        messages.error(request, 'We are facing some problem. We shall rectify it soon. Sorry for inconvenience caused.')
        return redirect('forget-password')  
    
    return render(request, 'account/fp_email_form.html')

#################### END PASSWORD RESET CHANGE ######################


def t_and_c(request):

    return render(request, 'account/terms_and_condition.html')