from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('horarios.apps.expocauca.views',

		#url(r'^add/plan/(?P<id_his>.*)/$','add_plan_view', name="vista_agregar_plan"),
		url(r'^expocauca/$', 'add_persona_view', name = 'vista_agregar_persona'),
		url(r'^editar/persona/(?P<id_prod>.*)/$', 'edit_persona_view', name = 'vista_editar_persona'),
	)