from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from django import forms
from flights.models import flight

# Create your views here.
class indexView(TemplateView):
    template_name = "index.html"

class formulario(forms.ModelForm):
    class Meta:
        model = flight
        fields = ["nombre", "tipo", "precio"]
        
class formularioView(View):
    template_name = "registrar.html"
    template_success = "index.html"
    
    def get(self, request): 
        form = formulario() 
        viewData = {}
        viewData["form"] = form
        return render(request, self.template_name, viewData)
    
    def post(self, request):
        form = formulario(request.POST)
        viewData = {}
        viewData["form"] = form
        if form.is_valid(): 
            form.save() 
            return render(request, self.template_success)
        else:
            form = formulario()
            return render(request, self.template_name, viewData)
        
        
class listarView(View):
    template_name = "listar.html"
    def get(self, request):
        viewData = {}
        vuelos = flight.objects.all()
        viewData ["vuelos"] = vuelos
        return render (request, self.template_name, viewData)