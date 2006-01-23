#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Autor: Josep Torrens Amer
# E-mail: toram74@gmail.com
#
# GNU GPL Licence, (C) 2005.
#
# Module: frmtaller
#
# Description: Modul de gestió dels tallers
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

class Frmtaller(AppBase):

	def __init__(self,  gjlib):
		
		AppBase.__init__(self, gjlib, root="frmtaller")

	#-- Frmtaller.new {
	def new(self):
		print "A new %s has been created" % self.__class__.__name__
	#-- Frmtaller.new }

	#-- Frmtaller custom methods {
	#   Write your own methods here
	#-- Frmtaller custom methods }

	#-- Frmtaller.on_bt_ta_nou_clicked {
	def on_bt_ta_nou_clicked(self, widget, *args):
		print "on_bt_ta_nou_clicked called with self.%s" % widget.get_name()
	#-- Frmtaller.on_bt_ta_nou_clicked }

	#-- Frmtaller.on_bt_ta_edita_clicked {
	def on_bt_ta_edita_clicked(self, widget, *args):
		print "on_bt_ta_edita_clicked called with self.%s" % widget.get_name()
	#-- Frmtaller.on_bt_ta_edita_clicked }

	#-- Frmtaller.on_bt_ta_esborra_clicked {
	def on_bt_ta_esborra_clicked(self, widget, *args):
		print "on_bt_ta_esborra_clicked called with self.%s" % widget.get_name()
	#-- Frmtaller.on_bt_ta_esborra_clicked }

	#-- Frmtaller.on_bt_ta_mecanics_clicked {
	def on_bt_ta_mecanics_clicked(self, widget, *args):
		print "on_bt_ta_mecanics_clicked called with self.%s" % widget.get_name()
	#-- Frmtaller.on_bt_ta_mecanics_clicked }

	#-- Frmtaller.on_button82_clicked {
	def on_button82_clicked(self, widget, *args):
		print "on_button82_clicked called with self.%s" % widget.get_name()
	#-- Frmtaller.on_button82_clicked }

	#-- Frmtaller.on_bt_ta_tanca_clicked {
	def on_bt_ta_tanca_clicked(self, widget, *args):
		print "on_bt_ta_tanca_clicked called with self.%s" % widget.get_name()
		self.hide_form()
	#-- Frmtaller.on_bt_ta_tanca_clicked }

	#-- Frmtaller.on_bt_ta_primer_clicked {
	def on_bt_ta_primer_clicked(self, widget, *args):
		print "on_bt_ta_primer_clicked called with self.%s" % widget.get_name()
	#-- Frmtaller.on_bt_ta_primer_clicked }

	#-- Frmtaller.on_bt_ta_anterior_clicked {
	def on_bt_ta_anterior_clicked(self, widget, *args):
		print "on_bt_ta_anterior_clicked called with self.%s" % widget.get_name()
	#-- Frmtaller.on_bt_ta_anterior_clicked }

	#-- Frmtaller.on_bt_ta_seguent_clicked {
	def on_bt_ta_seguent_clicked(self, widget, *args):
		print "on_bt_ta_seguent_clicked called with self.%s" % widget.get_name()
	#-- Frmtaller.on_bt_ta_seguent_clicked }

	#-- Frmtaller.on_bt_ta_darrer_clicked {
	def on_bt_ta_darrer_clicked(self, widget, *args):
		print "on_bt_ta_darrer_clicked called with self.%s" % widget.get_name()
	#-- Frmtaller.on_bt_ta_darrer_clicked }

	#-- Frmtaller.on_bt_ta_cerca_clicked {
	def on_bt_ta_cerca_clicked(self, widget, *args):
		print "on_bt_ta_cerca_clicked called with self.%s" % widget.get_name()
	#-- Frmtaller.on_bt_ta_cerca_clicked }

	#-- Frmtaller.on_bt_ta_aplica_clicked {
	def on_bt_ta_aplica_clicked(self, widget, *args):
		print "on_bt_ta_aplica_clicked called with self.%s" % widget.get_name()
	#-- Frmtaller.on_bt_ta_aplica_clicked }

	#-- Frmtaller.on_bt_ta_cancel_clicked {
	def on_bt_ta_cancel_clicked(self, widget, *args):
		print "on_bt_ta_cancel_clicked called with self.%s" % widget.get_name()
	#-- Frmtaller.on_bt_ta_cancel_clicked }
