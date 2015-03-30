from django.db import models
# -*- encoding: utf-8 -*-
# Create your models here.

class Jornada (models.Model):
	nombre 			= models.CharField(max_length = 256)
	def __unicode__ (self):
		return self.nombre


class Programa (models.Model):
	nombre 			= models.CharField(max_length = 256)
	def __unicode__ (self):
		return self.nombre

class Persona(models.Model):
	nombres_y_apellidos		= models.CharField(max_length = 256)
	telefono				= models.CharField(max_length = 256, unique = True)
	email					= models.EmailField(max_length = 500, null = True, blank = True)
	programa				= models.ManyToManyField(Programa)
	jornada 				= models.ForeignKey(Jornada, null = True, blank = True)
	fecha_registro  		= models.DateTimeField(auto_now = True)
	usuario 				= models.CharField(max_length = 500, null = True, blank = True)
	def __unicode__ (self):
		return self.nombres_y_apellidos