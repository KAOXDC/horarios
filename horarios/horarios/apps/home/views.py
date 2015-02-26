# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from horarios.apps.fichas.models import Horario, Evento, Franja, Ficha
from horarios.apps.home.forms import *
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect

def index_view (request):
	return render_to_response('home/index.html', context_instance = RequestContext(request))

def administrar_view(request):
	return render_to_response('home/administrar.html', context_instance = RequestContext(request))

def horarios_view (request):
	h = Horario.objects.filter()
	#e = h.eventos.all()
	#cat  = prod.categorias.all() #obtenemos las categorias del producto encontrado
	ctx = {'horarios':h}#, 'eventos':e}
	return render_to_response('home/horarios.html', ctx, context_instance = RequestContext(request))

def fichas_view(request):
	lists_fichas = Ficha.objects.all()
	ctx = {'fichas':lists_fichas}
	return render_to_response('home/fichas.html', ctx, context_instance = RequestContext(request))

def single_ficha_view (request, id_fic):
	f = Ficha.objects.get(id = id_fic)
	#apr = f.aprendices.all()
	lista_hor = Horario.objects.filter(ficha = id_fic)
	ctx = {'ficha':f, 'horarios': lista_hor}  #'aprendices':apr}
	return render_to_response('home/single_ficha.html',ctx, context_instance  = RequestContext(request))

def single_horario_ficha_view (request, id_hor):
	hor = Horario.objects.get(id = id_hor)
	print hor
	lista_eventos = Evento.objects.filter(horario = hor.id)
	print lista_eventos
	fra = []
	#fra = Evento.objects.filter(franja__in = lista_eventos )
	'''
				for f in lista_eventos:
					e = lista_eventos.objects.get(id = f.id)
					frajita = e.franja.all()
					fra.append(franjita)
			'''
	#fra = Franja.objects.filter()
	ctx = { 'horario':hor, 'eventos':lista_eventos, 'franjas':fra }
	return render_to_response('home/single_horario_ficha.html', ctx, context_instance = RequestContext(request))


def login_view(request):
	mensaje = ""
	if request.user.is_authenticated(): #verificamos si el usuario ya esta authenticado o logueado  
		return HttpResponseRedirect('/') #si esta logueado lo redirigimos a la pagina principal 
	else: #si no esta authenticado
		if request.method == "POST": 
			formulario = Login_form(request.POST) #creamos un objeto de Loguin_form
			if formulario.is_valid(): # si la informacion enviada es correcta
				usu = formulario.cleaned_data['usuario'] #guarda informacion ingresada del formulario
				pas = formulario.cleaned_data['clave'] #guarda informacion ingresada del formulario
				usuario = authenticate(username = usu, password = pas)#asigna la autenticacion del usuario
				if usuario is not None and usuario.is_active:# si el usuario no es nulo y esta activo
					login(request, usuario) #se loguea al sistema con la informacion de usuario
					return HttpResponseRedirect('/')# redirigimos a la pagina principal
				else:
					mensaje = "usuario y/o clave incorrecta"
		formulario = Login_form() #creamos un formulario nuevo en limpio
		ctx = {'form':formulario, 'mensaje':mensaje} # variable de contexto para pasar info a login.html
		return render_to_response('home/login.html', ctx, context_instance = RequestContext(request))

def logout_view(request):
	logout(request) #funcionde django importada anteriormente
	return HttpResponseRedirect('/') # redirigimos a la pagina principal



	'''

	fra = []
	eve = []
	
	fra = hor.eventos.franja.all()
	lista_eve = Evento.objects.all()
	eve = []
	for e in lista_eve:
		if e.id == hor.id:
			eve.append(e)
			
	
	his = Historia.objects.get(id=id_his)
	aux = 0
	evoluciones = []
	planes = []
	#pac =Paciente.objects.get(id = id_his)
	
	lista_his = Historia.objects.all()
	lista_evo = Evolucion.objects.all()
	lista_pla = Plan.objects.all()

	for h in lista_his:
		if h.id == his.id:
			aux = h

	#his = Historia.objects.get(id=id_his)
	for e in lista_evo:
		if e.historia.id == aux.id:
			evoluciones.append(e)

	for p in lista_pla:
		if p.historia.id == aux.id:
			planes.append(p)'''

	'''eve = hor.eventos.all()
				#preference = Preference.objects.get(**conditions)
				#Article.objects.filter(categories__in = preference.categories.all())	
				fra = Franja.objects.filter(nombre__in = eve)		
				#fra = Franja.objects.filter(id__in = eve.franja.all())
				lista_frajas = Franja.objects.all()
			'''
