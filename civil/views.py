from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages


from django.contrib.auth.decorators import login_required

from django.views.decorators.cache import cache_control

from payment.models import UserSubscription

from professional.models import Citation


# Create your views here.

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def civil_home(request):
    
    if request.method == "POST" and request.is_ajax():
    
      civil_sub_law = request.POST.get('subLawType[]')
      get_civil_court = request.POST.get('civilcourt[]')
      get_civil_category = request.POST.get('civilCategory[]')

      query = Citation.objects.values().filter(law_type__icontains ='civil' ,sub_law_type__icontains=  civil_sub_law, institution_name__icontains = get_civil_court, law_category__icontains =  get_civil_category).order_by('-date_of_order')

      if len(query) > 0:

        result = list(query)

        return JsonResponse({"status": "success", "result": result})
      elif len(query) == 0:
        return JsonResponse({"status": "nosuccess"})

      else:
        return JsonResponse({"status": "error"})


    
    else:
      subuser = request.user

      subscription = UserSubscription.objects.filter(user = subuser, is_active = True, paid = True)

      context = {
        'usersub': subscription,
      }
    

      return render(request, 'civil/civil_home.html', context)


@login_required(login_url='login')
def civil_search(request):

  if request.method == 'GET' and request.is_ajax():
    
    q = request.GET.get('q')

    if len(q) > 78 or len(q) < 1:
      return JsonResponse({"status": "empty"})
    
    else:
        
      q_JudgeName = Citation.objects.values().filter(law_type__contains ='civil',judge_name__contains = q)

      q_CaseNo = Citation.objects.values().filter(law_type__contains ='civil', case_no__contains = q)

      q_PartyName = Citation.objects.values().filter(law_type__contains ='civil', party_name__contains = q)

      q_AdvocatePetitioner = Citation.objects.values().filter(law_type__contains ='civil', advocate_petitioner__contains = q)

      q_AdvocateRespondent = Citation.objects.values().filter(law_type__contains ='civil', advocate_respondent__contains = q)

      q_DateOfOrder = Citation.objects.values().filter(law_type__contains ='civil', date_of_order__contains = q)

      query = q_JudgeName.union(q_CaseNo, q_PartyName, q_AdvocatePetitioner, q_AdvocateRespondent, q_DateOfOrder)

      if len(query) > 0:

        result = list(query)

        return JsonResponse({"status": "success", "result": result})
      elif len(query) == 0:
        result = q
        return JsonResponse({"status": "nosuccess","result": result})

      else:
        return JsonResponse({"status": "error"})
  else:

    return HttpResponse("404 not found")    

      
    

    
