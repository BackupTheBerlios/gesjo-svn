#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Autor: Josep Torrens Amer
# E-mail: toram74@gmail.com
#
# GNU GPL Licence, (C) 2005.
#
# Module: frmmecanic
#
# Description: Modul de gestió dels mecànics
#
# Version: 0.0.1
# 
# Created: 19-12-2005
#
# Modified: 28-12-2005
#

import os

import gtk

from appbase import AppBase

class Frmmecanic(AppBase):

	def __init__( self, gjlib ):
		
		AppBase.__init__(self, gjlib,  root="frmmecanic")

	#-- Frmmecanic.new {
	def new(self):
		print "A new %s has been created" % self.__class__.__name__
	#-- Frmmecanic.new }

	#-- Frmmecanic custom methods {
	
	#-- Frmmecanic custom methods }

	#-- Frmmecanic.on_bt_me_nou_clicked {
	def on_bt_me_nou_clicked(self, widget, *args):
		"""
		Entra un nou marca
		"""
		print "Nou mecànic"
		self.nova_fitxa("me")
		
	#-- Frmmecanic.on_bt_me_nou_clicked }

	#-- Frmmecanic.on_bt_me_edita_clicked {
	def on_bt_me_edita_clicked(self, widget, *args):
		"""
		Edita el marca
		"""
		print "Editam marca"
		self.editam_fitxa("me")
	#-- Frmmecanic.on_bt_me_edita_clicked }

	#-- Frmmecanic.on_bt_me_esborra_clicked {
	def on_bt_me_esborra_clicked(self, widget, *args):
		"""
		Esborra un marca
		"""
		print "Esborra marca"
		self.esborra_fitxa("ma")
	#-- Frmmecanic.on_bt_me_esborra_clicked }

	#-- Frmmecanic.on_bt_me_tallers_clicked {
	def on_bt_me_tallers_clicked(self, widget, *args):
		print "on_bt_me_tallers_clicked called with self.%s" % widget.get_name()
	#-- Frmmecanic.on_bt_me_tallers_clicked }

	#-- Frmmecanic.on_bt_me_imprimeix_clicked {
	def on_bt_me_imprimeix_clicked(self, widget, *args):
		pass
	#-- Frmmecanic.on_bt_me_imprimeix_clicked }
	
	#-- Frmmecanic.on_bt_me_tanca_clicked {
	def on_bt_me_tanca_clicked(self, widget, *args):
		print "on_bt_me_tanca_clicked called with self.%s" % widget.get_name()
		self.hide_form()
	#-- Frmmecanic.on_bt_me_tanca_clicked }

	#-- Frmmecanic.on_bt_me_cerca_taller_clicked {
	def on_bt_me_cerca_taller_clicked(self, widget, *args):
		print "on_bt_me_cerca_taller_clicked called with self.%s" % widget.get_name()
	#-- Frmmecanic.on_bt_me_cerca_taller_clicked }

	#-- Frmmecanic.on_bt_me_primer_clicked {
	def on_bt_me_primer_clicked(self, widget, *args):
		"""
		Anam al primer marca
		"""
		self.primera_fitxa("me")
		
	#-- Frmmecanic.on_bt_me_primer_clicked }

	#-- Frmmecanic.on_bt_me_anterior_clicked {
	def on_bt_me_anterior_clicked(self, widget, *args):
		"""
		Anam al marca anterior
		"""
		self.anterior_fitxa("me")

	#-- Frmmecanic.on_bt_me_anterior_clicked }

	#-- Frmmecanic.on_bt_me_seguent_clicked {
	def on_bt_me_seguent_clicked(self, widget, *args):
		"""
		Anam al marca següent
		"""
		self.seguent_fitxa("me")

	#-- Frmmecanic.on_bt_me_seguent_clicked }

	#-- Frmmecanic.on_bt_me_darrer_clicked {
	def on_bt_me_darrer_clicked(self, widget, *args):
		"""
		Anam al darrer marca
		"""
		self.darrera_fitxa("me")

	#-- Frmmecanic.on_bt_me_darrer_clicked }

	#-- Frmmecanic.on_bt_me_cerca_clicked {
	def on_bt_me_cerca_clicked(self, widget, *args):
		"""
		Cercam un marca
		"""
		self.cerca_fitxa("me")
		
	#-- Frmmecanic.on_bt_me_cerca_clicked }

	#-- Frmmecanic.on_bt_me_aplica_clicked {
	def on_bt_me_aplica_clicked(self, widget, *args):
		"""
		Acepta l'entrada de marcas
		"""
		print "Aceptam nou/edicio marca"
		self.aceptam_fitxa("me")
		
	#-- Frmmecanic.on_bt_me_aplica_clicked }

	#-- Frmmecanic.on_bt_me_cancel_clicked {
	def on_bt_me_cancel_clicked(self, widget, *args):
		"""
		Cancela l'entrada de marcas
		"""
		print "Cancelam nou/edicio marca"
		self.cancelam_fitxa("me")

	#-- Frmmecanic.on_bt_me_cancel_clicked }



