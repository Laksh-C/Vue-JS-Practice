from typing import List
from django.shortcuts import render
from django.http import HttpResponse
from .models import practice
from django.db.models import Q
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

from .forms import ProductCreateForm
from django.urls import reverse_lazy


'''
# Create your views here.
def homepage(request):
    practice_obj = practice.objects.all()
    return render(request, 'home.html', {'practice': practice_obj})
'''

class homepage(ListView):
    model = practice
    template_name = "home.html"

    #{'practice': practice_obj}

'''
class postinfo(request, ListView):
    if(request.method == 'POST'):
        title_name = request.POST.get("title_name")
        description_name = request.POST.get("description_name")
        price_name = request.POST.get("price_name")
        instance = practice(title = title_name, description = description_name, price = price_name)
        instance.save()
        
        practice_obj = practice.objects.all()
        return render(request, 'home.html', {'practice': practice_obj})
        
        model = practice
        template_name = "home.html"

'''

class postinfo(CreateView):


    form_class = ProductCreateForm
    template_name = "insert.html"
    success_url = reverse_lazy("home")
