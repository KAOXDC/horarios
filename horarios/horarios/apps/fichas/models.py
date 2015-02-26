from django.db import models

# Create your models here.

dias_semana = (
	('lunes', 'Lunes'),
	('martes', 'Martes'),
	('miercoles', 'Miercoles'),
	('jueves','Jueves'),
	('viernes','Viernes'),
)
class Tipo_Programa (models.Model):
	nombres 		= models.CharField(max_length = 140)
	

class Jornada (models.Model):
	nombre 			= models.CharField(max_length = 140)

	def __unicode__(self):
		return self.nombre
	
class Ficha(models.Model):
	identificador	= models.CharField(max_length = 140)
	jornada			= models.ForeignKey(Jornada)
	#aprendices 		= models.ManyToManyField(Aprendiz)
	def __unicode__(self):
		return self.identificador

class Programa (models.Model):
	nombre 			= models.CharField(max_length = 140)
	tipo 			= models.ForeignKey(Tipo_Programa)
	fichas			= models.ManyToManyField(Ficha)

	def __unicode__(self):
		return self.nombre


class Aprendiz (models.Model):
	#documento 		= models.CharField(max_length=15)
	nombres 		= models.CharField(max_length = 140)
	apellidos 		= models.CharField(max_length = 140)
	#correo 			= models.EmailField(max_length=140)
	estado			= models.BooleanField(default = True)
	#tipo_de_persona = models.ForeignKey(Tipo_Persona)
	#tipo_documento 	= models.CharField(Tipo_documento)
	ficha 			= models.ForeignKey(Ficha)
	programa 		= models.ForeignKey(Programa)

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
	nombre 			= models.CharField(max_length = 140)
	jornada 		= models.ForeignKey(Jornada)

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