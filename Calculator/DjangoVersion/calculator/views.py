from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json 

from . import models

def Home(request):
    return render(
        request,
        "calculator/home.html",
        {}
    )

@csrf_exempt
def History(request):
    his = models.History()
    data = json.load(request)
    his.total = data.get("total")
    his.string = data.get("string")
    his.save()
    return JsonResponse({'w': "work!"})