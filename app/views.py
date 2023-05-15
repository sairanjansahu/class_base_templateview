
from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import TemplateView
from app.forms import *
from django.http import HttpResponse

# Create your views here.
class cbv_context(TemplateView):
    template_name='cbv_context.html'
    def get_context_data(self, **kwargs):
        edco= super().get_context_data(**kwargs)
        edco['name']='raj'
        edco['age']=23
        return edco

class cbv_form(TemplateView):
    template_name='cbv_form.html'
    def get_context_data(self, **kwargs):
        eot= super().get_context_data(**kwargs)
        to=TopicForm()
        eot['to']=to
        return eot
    
    def post(self,request):
        tod=TopicForm(request.POST)
        if tod.is_valid():
            tod.save()
            return HttpResponse('insertion done succesfully')