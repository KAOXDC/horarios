from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('horarios.apps.home.views',
		url(r'^$','index_view', name = 'vista_principal'),
		url(r'^horarios/$','horarios_view', name = 'vista_horarios'),
		url(r'^horario/(?P<id_hor>.*)/$', 'single_horario_ficha_view', name = 'vista_horario_ficha'),
		url(r'^fichas/$','fichas_view', name = 'vista_fichas'),
		url(r'^ficha/(?P<id_fic>.*)/$', 'single_ficha_view', name = 'vista_single_ficha'),
		url(r'^administrar/$','administrar_view', name = 'vista_administrar'),
		url(r'^login/$', 'login_view', name = 'vista_login'),
		url(r'^logout/$', 'logout_view', name = 'vista_logout'),

		
		url(r'^instructores/$','instructores_view', name = 'vista_instructores'),
		url(r'^instructor/(?P<id_ins>.*)/$', 'single_instructor_view', name = 'vista_instructor_ficha'),
		url(r'^franjas/$','franjas_view', name = 'vista_franjas'),
		url(r'^franja/(?P<id_franja>.*)/$', 'single_franja_view', name = 'vista_single_franja'),
		
		#url(r'^productos/$', 'productos_view', name = 'vista_productos'),
		#url(r'^productos/page/(?P<pagina>.*)/$', 'productos_view', name = 'vista_productos'),
		#url(r'^producto/(?P<id_prod>.*)/$', 'single_product_view', name = 'vista_single_producto'),
		#url(r'^contacto/$', 'contacto_view', name = 'vista_contacto'),
	)