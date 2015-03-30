# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from horarios.apps.expocauca.models import *
from datetime import date 
from horarios.apps.expocauca.forms import *

def add_persona_view(request):
	personas = []
	if request.method == "POST":
		formulario = add_persona_form(request.POST)
		if formulario.is_valid():
			add = formulario.save(commit = False)
			#add.status = True
			add.save() # guarda la informacion
			formulario.save_m2m() # guarda las relaciones ManyToMany
			info = "Guardado Satisfactoriamente"
			return HttpResponseRedirect ('/expocauca')
	else:
		formulario = add_persona_form()
		try:
			personas = Persona.objects.all()	
		except:
			personas = []
	ctx = {'form':formulario, 'personas':personas}
	return render_to_response('expocauca/add_persona.html', ctx,context_instance = RequestContext(request))

def edit_persona_view(request, id_prod):
	info = ""
	prod = Persona.objects.get(pk = id_prod)
	if request.method == "POST":
		formulario = add_persona_form(request.POST, request.FILES, instance= prod)
		if formulario.is_valid():
			edit_prod = formulario.save(commit = False)
			formulario.save_m2m()
			#edit_prod.status = True
			edit_prod.save()
			info = "Guardado Satisfactoriamente"
			return HttpResponseRedirect('/expocauca/')
	else:
		formulario = add_persona_form(instance = prod)
	ctx = {'form':formulario, 'informacion':info}
	return render_to_response('expocauca/add_persona.html', ctx,context_instance = RequestContext(request))
