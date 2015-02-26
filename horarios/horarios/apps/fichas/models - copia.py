from django.db import models

# Create your models here.

dias_semana = (
	('lunes', 'Lunes'),
	('martes', 'Martes'),
	('miercoles', 'Miercoles'),
	('jueves','Jueves'),
	('viernes','Viernes'),
)

class Aprendiz (models.Model):
	#documento 		= models.CharField(max_length=15)
	nombres 		= models.CharField(max_length = 140)
	apellidos 		= models.CharField(max_length = 140)
	#correo 			= models.EmailField(max_length=140)
	estado			= models.BooleanField(default = True)
	#tipo_de_persona = models.ForeignKey(Tipo_Persona)
	#tipo_documento 	= models.CharField(Tipo_documento)
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
	def __unicode__(self):
		return self.nombres

class Ficha(models.Model):
	identificador	= models.CharField(max_length = 140)
	aprendices 		= models.ManyToManyField(Aprendiz)
	def __unicode__(self):
		return self.identificador

class Horario(models.Model):
	fecha 			= models.DateField()
	ficha 			= models.ForeignKey(Ficha)
	#eventos 		= models.ForeignKey(Evento)
	def __unicode__(self):
		return self.ficha.identificador

class Franja(models.Model):
	nombre 			= models.CharField(max_length = 140)
	def __unicode__(self):
		return self.nombre

class Evento(models.Model):
	dias 			= models.CharField(max_length = 20, choices = dias_semana )
	instructor 		= models.ForeignKey(Instructor)
	franja 			= models.ManyToManyField(Franja)
	horario 		= models.ForeignKey(Horario)
	def __unicode__(self):
		return self.dias



'''
5434 2110 0457 7894
7894-567
10 16



'''