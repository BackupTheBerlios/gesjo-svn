﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python module prova.py
# Autogenerated from prova
# Generated on Thu Sep  1 12:12:14 2005

# Warning: Do not modify any context comment such as #--
# They are required to keep user's code


import gtk

from appbase import AppBase



DEBUG = 1

class Frmrecercador(AppBase):

	def __init__(self, pCamps, gjlib ):
		
		AppBase.__init__(self, gjlib, root="frm_cercador")
		self.camps = pCamps
		self.res = {}
		
		fila = 0
		self.taula = self.get_widget("taula")
		self.taula.resize(len(self.camps.obte_camps_cerca()),2)
		
		for x in self.camps.obte_camps_cerca():
			
			etiqueta = gtk.Label(self.camps.obte_etiqueta(x))
			etiqueta.show()
			self.taula.attach(etiqueta,0,1,fila,fila+1)
			
			entrada = gtk.Entry()
			entrada.set_name(x)
			entrada.show()
			self.taula.attach(entrada,1,2,fila,fila+1)
			
			fila += 1	


	#-- FrmCercador.new {
	def new(self):
		if DEBUG: print "A new %s has been created" % self.__class__.__name__
	#-- FrmCercador.new }

	#-- FrmCercador custom methods {
	def run(self):
		self.show_form()
		
		AppBase.run( self )
		
		self.hide_form()
		return self.res

	#-- FrmCercador custom methods }

	#-- FrmCercador.on_cercar {
	def on_cercar(self, widget, *args):
		if DEBUG: print "on_cercar called with self.%s" % widget.get_name()
		
		fills = self.taula.get_children()
		entrades = [x for x in fills if (type(x) is gtk.Entry)]
		camps = [x.name for x in entrades]
		valors = [x.get_text() for x in entrades ] 
		
		self.res = dict(zip(camps, valors)) 
		
		self.quit()
	#-- FrmCercador.on_cercar }

	#-- FrmCercador.on_cancelar {
	def on_cancelar(self, widget, *args):
		if DEBUG: print "on_cancelar called with self.%s" % widget.get_name()
		
		self.quit()
	#-- FrmCercador.on_cancelar }

