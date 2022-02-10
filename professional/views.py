
from django.shortcuts import render

from django.contrib.auth.decorators import login_required

from django.views.decorators.cache import cache_control

from payment.models import UserSubscription

from . models import Citation


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def professional_home(request):

   subuser = request.user

   subscription = UserSubscription.objects.filter(user = subuser, is_active = True)

   context = {
      'usersub': subscription,
   }
   
   return render(request, 'professional/professional_home.html', context)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def detail_doc(request,id):

   subuser = request.user

   subscription = UserSubscription.objects.filter(user = subuser, is_active = True)

   try:
      query = Citation.objects.get(pk = id)
   except Exception as e:
      print(e)

   context = {
      'usersub': subscription,
      'query': query,
   }
   return render(request, 'professional/detaildoc.html', context)