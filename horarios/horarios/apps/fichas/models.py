#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

dias_semana = (
	('lunes', 'Lunes'),
	('martes', 'Martes'),
	('miercoles', 'Miercoles'),
	('jueves','Jueves'),
	('viernes','Viernes'),
)
jornadas = (
	('m', 'Mañana'),
	('t', 'Tarde'),
	('n', 'Noche'),

)

fases = (
	('analisis','analisis'),
	('diseño','diseño'),
	('desarrollo','desarrollo'),
	('implantacion','implantacion'),
	
)


class Tipo_Programa (models.Model):
	nombres 		= models.CharField(max_length = 140, unique = True)
	def __unicode__(self):
		return self.nombres

class Jornada (models.Model):
	nombre 			= models.CharField(max_length = 140)
	def __unicode__(self):
		return self.nombre

class Programa (models.Model):
	nombre 			= models.CharField(max_length = 140, unique = True)
	tipo 			= models.ForeignKey(Tipo_Programa)
	#fichas			= models.ManyToManyField(Ficha)

	def __unicode__(self):
		return self.nombre

class Competencia (models.Model):
	codigo 			= models.CharField(max_length = 140)
	nombre 			= models.CharField(max_length = 140)
	programa		= models.ManyToManyField(Programa)
	fase 			= models.CharField(max_length = 140, choices = fases)

	def __unicode__(self):
		return self.nombre

class Resultados (models.Model):
	codigo 			= models.CharField(max_length = 140)
	nombre 			= models.CharField(max_length = 140)
	competencia 	= models.ForeignKey(Competencia)
	def __unicode__(self):
		return self.nombre

class Ficha(models.Model):
	identificador	= models.CharField(max_length = 140, unique = True)
	jornada			= models.CharField(max_length = 140, choices=jornadas)
	#aprendices 		= models.ManyToManyField(Aprendiz)
	programa 		= models.ForeignKey(Programa)

	def __unicode__(self):
		return self.identificador

class Aprendiz (models.Model):
	#documento 		= models.CharField(max_length=15)
	nombres 		= models.CharField(max_length = 140)
	apellidos 		= models.CharField(max_length = 140)
	#correo 			= models.EmailField(max_length=140)
	estado			= models.BooleanField(default = True)
	#tipo_de_persona = models.ForeignKey(Tipo_Persona)
	#tipo_documento 	= models.CharField(Tipo_documento)
	ficha 			= models.ForeignKey(Ficha)

	def __unicode__(self):
		return self.nombres

class Instructor (models.Model): 		
	#documento 		= models.CharField(max_length=15)
	nombres 		= models.CharField(max_length = 140)
	apellidos 		= models.CharField(max_length = 140)
	#correo 			= models.EmailField(max_length=140)
	estado			= models.BooleanField(default = True)
	#tipo_de_persona = models.ForeignKey(Tipo_Persona)
	#tipo_documento 	= models.CharField(Tipo_documento)
	fichas 			= models.ManyToManyField(Ficha)

	def __unicode__(self):
		return self.nombres

class Horario(models.Model):
	fecha 			= models.DateField()
	ficha 			= models.ForeignKey(Ficha)
	#eventos 		= models.ForeignKey(Evento)

	def __unicode__(self):
		return self.ficha.identificador

class Franja(models.Model):
	nombre 			= models.CharField(max_length = 140, unique = True)
	jornada			= models.CharField(max_length = 140, choices=jornadas)
	#jornada 		= models.ForeignKey(Jornada)

	def __unicode__(self):
		return self.nombre

class Evento(models.Model):
	dias 			= models.CharField(max_length = 20, choices = dias_semana )
	instructor 		= models.ForeignKey(Instructor)
	franja 			= models.ManyToManyField(Franja)
	horario 		= models.ForeignKey(Horario)
	competencia		= models.ForeignKey(Competencia)
	#resultados		= models.ForeignKey(Resultados)
	def __unicode__(self):
		return self.dias



'''
SERIAL: 5434 2110 0457 7894
CODE: 7894-567
VERSION: 10.16
'''

