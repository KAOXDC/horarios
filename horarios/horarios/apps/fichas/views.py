# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from horarios.apps.fichas.models import Ficha, Evento, Horario
from horarios.apps.fichas.forms import add_horario_form, add_evento_form, add_instructor_form, add_aprendiz_form
from datetime import date 

def add_instructor_view(request):
	if request.method == "POST":
		formulario = add_instructor_form(request.POST)
		if formulario.is_valid():
			add = formulario.save(commit = False)
			#add.status = True
			add.save() # guarda la informacion
			#formulario.save_m2m() # guarda las relaciones ManyToMany
			info = "Guardado Satisfactoriamente"
			return HttpResponseRedirect ('/')
	else:
		formulario = add_instructor_form()
	ctx = {'form':formulario}
	return render_to_response('fichas/add_instructor.html', ctx,context_instance = RequestContext(request))

def add_aprendiz_view(request):
	if request.method == "POST":
		formulario = add_aprendiz_form(request.POST)
		if formulario.is_valid():
			add = formulario.save(commit = False)
			#add.status = True
			add.save() # guarda la informacion
			#formulario.save_m2m() # guarda las relaciones ManyToMany
			info = "Guardado Satisfactoriamente"
			return HttpResponseRedirect ('/')
	else:
		formulario = add_aprendiz_form()
	ctx = {'form':formulario}
	return render_to_response('fichas/add_aprendiz.html', ctx,context_instance = RequestContext(request))


def add_horario_view (request, id_fic):
	now = date.today()
	fic = Ficha.objects.get(id = id_fic)
	if request.method == "POST":
		form_horario = add_horario_form(request.POST, prefix = "hor")
		if form_horario.is_valid():
			hor = form_horario.save(commit=False)
			hor.ficha = fic
			hor.fecha = now
			hor.save()
			info = "Horario Guardado Satisfactoriamente"
			return HttpResponseRedirect('/ficha/%s' %fic.id)
		else:
			info = "Fallo en el registro del Horario"
	else:
		form_horario = add_horario_form(prefix = "hor")
	
	ctx = {'form_horario':form_horario, 'fic':fic}
	return render_to_response('fichas/add_horario.html', ctx, context_instance = RequestContext(request))

def add_evento_view (request, id_hor):
	now = date.today()
	hor = Horario.objects.get(id = id_hor)
	#fic = Ficha.objects.get(id = id_fic)
	if request.method == "POST":
		form_evento = add_evento_form(request.POST, prefix = "eve")
		if form_evento.is_valid():
			eve = form_evento.save(commit=False)
			eve.horario = hor
			eve.save()
			form_evento.save_m2m()
			info = "Horario Guardado Satisfactoriamente"
			return HttpResponseRedirect('/horario/%s' %hor.id)
		else:
			info = "Fallo en el registro del Horario"
	else:
		form_evento = add_evento_form(prefix = "eve")
	
	ctx = {'form_evento':form_evento, 'hor':hor}
	return render_to_response('fichas/add_evento.html', ctx, context_instance = RequestContext(request))



'''
def add_product_view(request):
	info = "inicializando"
	if request.method == "POST":
		formulario = add_product_form(request.POST, request.FILES)
		if formulario.is_valid():
			add = formulario.save(commit = False)
			add.status = True
			add.save() # guarda la informacion
			formulario.save_m2m() # guarda las relaciones ManyToMany
			info = "Guardado Satisfactoriamente"
			return HttpResponseRedirect ('/producto/%s' %add.id)
	else:
		formulario = add_product_form()
	ctx = {'form':formulario, 'informacion':info}
	return render_to_response('ventas/add_producto.html', ctx,context_instance = RequestContext(request))

'''



'''

def add_plan_view(request, id_his):
	if request.user.is_authenticated():
		now = date.today()
		his = Historia.objects.get(id = id_his)
		if request.method == "POST":
			form_pla = addPlanForm(request.POST, prefix = "pla")
			if form_pla.is_valid():
				pla = form_pla.save(commit = False)
				pla.historia = his
				pla.fecha = now
				pla.save()
				info = "Evolucion Guardado Satisfactoriamente"
				return HttpResponseRedirect ('/historia/%s'%his.id)
			else:
				info = "Fallo el Registro de Evolucion"
		else:
			form_pla = addPlanForm(prefix = "pla")
		ctx =  {'form_pla':form_pla, 'his':his}
		return render_to_response ('historias/addplan.html', ctx,  context_instance = RequestContext(request))
	else:
		return HttpResponseRedirect('/')
	
'''