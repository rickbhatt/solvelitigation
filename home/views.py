from django.shortcuts import render

from django.views.decorators.cache import cache_control

from django.contrib.auth.decorators import login_required


# ******************* VIEWS AND MODELS FROM SAME APP ************************

from .decorators import IfAuthenticatedUser

from payment.models import ServiceProduct

# ********************* END OF VIEWS AND MODELS FROM SAME APP ********************    



# ******************* VIEWS AND MODELS FROM OTHER APPS ************************

from analytics.views import get_ip, visitor_count


# ********************* END OF VIEWS AND MODELS FROM OTHER APPS ********************    

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@IfAuthenticatedUser
def home(request):

    ip = get_ip(request)

    visitor_count(ip)
    
    return render(request, 'home/index.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@IfAuthenticatedUser
def subscription(request):

    civil = ServiceProduct.objects.filter(title = 'Civil')

    criminal = ServiceProduct.objects.filter(title = "Criminal")

    tax =  ServiceProduct.objects.filter(title = 'Taxation')

    service = ServiceProduct.objects.filter(title = "Service")

    corp = ServiceProduct.objects.filter(title= "Corporate")


    for cv in civil:
        cv_monthly = cv.monthly_price
        cv_quaterly = cv.quaterly_price
        cv_hf = cv.hf_price

    for cr in criminal:

        cr_monthly = cr.monthly_price
        cr_quaterly = cr.quaterly_price
        cr_hf = cr.hf_price

    for tx in tax:

        tx_monthly = tx.monthly_price
        tx_quaterly = tx.quaterly_price
        tx_hf = tx.hf_price

    for sv in service:

        sv_monthly = sv.monthly_price
        sv_quaterly = sv.quaterly_price
        sv_hf = sv.hf_price

    for crp in corp:

        crp_monthly = crp.monthly_price
        crp_quaterly = crp.quaterly_price
        crp_hf = crp.hf_price
    
    context = {
        'cv_monthly':cv_monthly,
        'cv_quaterly':cv_quaterly,
        'cv_hf':cv_hf,
        'cr_monthly':cr_monthly,
        'cr_quaterly':cr_quaterly,
        'cr_hf':cr_hf,
        'tx_monthly':tx_monthly,
        'tx_quaterly':tx_quaterly,
        'tx_hf':tx_hf,
        'sv_monthly':sv_monthly,
        'sv_quaterly':sv_quaterly,
        'sv_hf':sv_hf,
        'crp_monthly':crp_monthly,
        'crp_quaterly':crp_quaterly,
        'crp_hf':crp_hf
    
    }

    return render(request, 'home/subscription.html', context)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def contact_us(request):
     
    return render(request, 'home/contact_us.html')



def launching_soon(request):

    return render(request, 'home/launch_soon.html')