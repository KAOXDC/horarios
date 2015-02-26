from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('horarios.apps.fichas.views',

		#url(r'^add/plan/(?P<id_his>.*)/$','add_plan_view', name="vista_agregar_plan"),
		url(r'^add/horario/(?P<id_fic>.*)/$', 'add_horario_view', name = 'vista_agregar_horario'),
		url(r'^add/evento/(?P<id_hor>.*)/$', 'add_evento_view', name = 'vista_agregar_evento'),
		url(r'^add/instuctor/$','add_instructor_view', name = 'vista_agregar_instructor'),
		url(r'^add/aprendiz/$','add_aprendiz_view', name = 'vista_agregar_aprendiz'),		
	)