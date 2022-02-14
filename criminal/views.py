from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages


from django.contrib.auth.decorators import login_required

from django.views.decorators.cache import cache_control

from payment.models import UserSubscription

from professional.models import Citation

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def criminal_home(request):

    subuser = request.user

    subscription = UserSubscription.objects.filter(user = subuser, is_active = True, paid=True)

    context = {
        'usersub': subscription,
      }
    

    return render(request, 'criminal/criminal_home.html', context)