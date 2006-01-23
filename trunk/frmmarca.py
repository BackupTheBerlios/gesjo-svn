#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Autor: Josep Torrens Amer
# E-mail: toram74@gmail.com
#
# GNU GPL Licence, (C) 2005.
#
# Module: frmmarca
#
# Description: Modul de gestió de les marques
#
# Version: 0.0.1
# 
# Created: 19-12-2005
#
# Modified:19-12-2005
#

import os

import gtk

from appbase import AppBase

class Frmmarca(AppBase):

	def __init__(self, gjlib 	):
		
		AppBase.__init__(self,  gjlib,  root="frmmarca")

	#-- Frmmarca.new {
	def new(self):
		print "A new %s has been created" % self.__class__.__name__
	#-- Frmmarca.new }		self.frmmarca.get_wi

	#-- Frmmarca custom methods {
		
	
	
	#-- Frmmarca custom methods }

	#-- Frmmarca.on_bt_ma_nou_clicked {
	def on_bt_ma_nou_clicked(self, widget, *args):
		"""
		Entra un nou marca
		"""
		print "Nou marca"
		self.nova_fitxa("ma")
		
	#-- Frmmarca.on_bt_ma_nou_clicked }

	#-- Frmmarca.on_bt_ma_edita_clicked {
	def on_bt_ma_edita_clicked(self, widget, *args):
		"""
		Edita el marca
		"""
		print "Editam marca"
		self.editam_fitxa("ma")
		
	#-- Frmmarca.on_bt_ma_edita_clicked }

	#-- Frmmarca.on_bt_ma_esborra_clicked {
	def on_bt_ma_esborra_clicked(self, widget, *args):
		"""
		Esborra un marca
		"""
		print "Esborra marca"
		self.esborra_fitxa("ma")
		
	#-- Frmmarca.on_bt_ma_esborra_clicked }

	#-- Frmmarca.on_bt_cl_arreglos_clicked {
	def on_bt_cl_arreglos_clicked(self, widget, *args):
		print "on_bt_cl_arreglos_clicked called with self.%s" % widget.get_name()
	#-- Frmmarca.on_bt_cl_arreglos_clicked }

	#-- Frmmarca.on_bt_cl_imprimeix_clicked {
	def on_bt_cl_imprimeix_clicked(self, widget, *args):
		print "on_bt_cl_imprimeix_clicked called with self.%s" % widget.get_name()
	#-- Frmmarca.on_bt_cl_imprimeix_clicked }

	#-- Frmmarca.on_bt_ma_tanca_clicked {
	def on_bt_ma_tanca_clicked(self, widget, *args):
		print "on_bt_ma_tanca_clicked called with self.%s" % widget.get_name()
		self.hide_form()
		
	#-- Frmmarca.on_bt_ma_tanca_clicked }

	#-- Frmmarca.on_bt_ma_primer_clicked {
	def on_bt_ma_primer_clicked(self, widget, *args):
		"""
		Anam al primer marca
		"""
		self.primera_fitxa("ma")
		
	#-- Frmmarca.on_bt_ma_primer_clicked }

	#-- Frmmarca.on_bt_ma_anterior_clicked {
	def on_bt_ma_anterior_clicked(self, widget, *args):
		"""
		Anam al marca anterior
		"""
		self.anterior_fitxa("ma")

	#-- Frmmarca.on_bt_ma_anterior_clicked }

	#-- Frmmarca.on_bt_ma_seguent_clicked {
	def on_bt_ma_seguent_clicked(self, widget, *args):
		"""
		Anam al marca següent
		"""
		self.seguent_fitxa("ma")

	#-- Frmmarca.on_bt_ma_seguent_clicked }

	#-- Frmmarca.on_bt_ma_darrer_clicked {
	def on_bt_ma_darrer_clicked(self, widget, *args):
		"""
		Anam al darrer marca
		"""
		self.darrera_fitxa("ma")


	#-- Frmmarca.on_bt_ma_darrer_clicked }

	#-- Frmmarca.on_bt_ma_cerca_clicked {
	def on_bt_ma_cerca_clicked(self, widget, *args):
		"""
		Cercam un marca
		"""
		self.cerca_fitxa("ma")
		
	#-- Frmmarca.on_bt_ma_cerca_clicked }

	#-- Frmmarca.on_bt_ma_aplica_clicked {
	def on_bt_ma_aplica_clicked(self, widget, *args):
		"""
		Acepta l'entrada de marcas
		"""
		print "Aceptam nou/edicio marca"
		self.aceptam_fitxa("ma")
		
	#-- Frmmarca.on_bt_ma_aplica_clicked }

	#-- Frmmarca.on_bt_ma_cancel_clicked {
	def on_bt_ma_cancel_clicked(self, widget, *args):
		"""
		Cancela l'entrada de marcas
		"""
		print "Cancelam nou/edicio marca"
		self.cancelam_fitxa("ma")

	#-- Frmmarca.on_bt_ma_cancel_clicked }

