#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from django.forms.extras import SelectDateWidget
from django.contrib.admin import widgets
from horarios.apps.fichas.models import *

class add_horario_form (forms.ModelForm):
	#fecha = forms.DateField(widget=forms.TextInput(attrs={'id':'datepicker'}))
	fecha = forms.DateField(widget = forms.TextInput(attrs={'id':'datepicker'}), label='Fecha del Horario ')	
	class Meta:
		model = Horario
		exclude = ('ficha',)

class add_evento_form_M (forms.ModelForm):
	#franja = forms.ModelMultipleChoiceField(queryset=Franja.objects.filter(jornada__nombre = 'Tarde'), required=False, widget=forms.CheckboxSelectMultiple)
	franja = forms.ModelMultipleChoiceField(queryset=Franja.objects.filter(jornada = 'm'), required=False)
	class Meta:
		model = Evento
		exclude = ('horario',)
class add_evento_form_T (forms.ModelForm):
	#franja = forms.ModelMultipleChoiceField(queryset=Franja.objects.filter(jornada__nombre = 'Tarde'), required=False, widget=forms.CheckboxSelectMultiple)
	franja = forms.ModelMultipleChoiceField(queryset=Franja.objects.filter(jornada = 't'), required=False)
	class Meta:
		model = Evento
		exclude = ('horario',)
class add_evento_form_N (forms.ModelForm):
	#franja = forms.ModelMultipleChoiceField(queryset=Franja.objects.filter(jornada__nombre = 'Tarde'), required=False, widget=forms.CheckboxSelectMultiple)
	franja = forms.ModelMultipleChoiceField(queryset=Franja.objects.filter(jornada = 'n'), required=False)
	class Meta:
		model = Evento
		exclude = ('horario',)
class add_evento_form (forms.ModelForm):
	#franja = forms.ModelMultipleChoiceField(queryset=Franja.objects.filter(jornada__nombre = 'Tarde'), required=False, widget=forms.CheckboxSelectMultiple)
	#franja = forms.ModelMultipleChoiceField(queryset=Franja.objects.filter(jornada__nombre = ), required=False)
	class Meta:
		model = Evento
		exclude = ('horario',)

class add_instructor_form (forms.ModelForm):
	class Meta:
		model = Instructor
		
class add_aprendiz_form (forms.ModelForm):
	class Meta:
		model = Aprendiz

class add_ficha_form (forms.ModelForm):
	class Meta:
		model = Ficha

class add_tipo_programa_form(forms.ModelForm):
	class Meta:
		model = Tipo_Programa

class add_programa_form(forms.ModelForm):
	class Meta:
		model = Programa

class add_franja_form(forms.ModelForm):
	class Meta:
		model = Franja
