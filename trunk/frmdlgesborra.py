#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Autor: Josep Torrens Amer
# E-mail: toram74@gmail.com
#
# GNU GPL Licence, (C) 2005.
#
# Module: dlgesborra
#
# Description: Modul de diàlegs d'esborrar
#
# Version: 0.0.1
# 
# Created: 28-12-2005
#
# Modified:28-12-2005
#

import os

import gtk


from appbase import AppBase

class FrmDlEsborra(AppBase):

	def __init__(self, gjlib):
		
		AppBase.__init__(self, gjlib, root="frm_dl_esborra")
		self.esborra = False
	#-- FrmDlEsborra.new {
	def new(self):
		print "A new %s has been created" % self.__class__.__name__
	#-- FrmDlEsborra.new }

	#-- FrmDlEsborra custom methods {
	def run(self):
		self.show_form()
		
		AppBase.run( self )
		
		self.hide_form()
		return self.esborra
	#-- FrmDlEsborra custom methods }

	#-- FrmDlEsborra.on_bt_dl_esborra_cancel_clicked {
	def on_bt_dl_esborra_cancel_clicked(self, widget, *args):
		print "on_bt_dl_esborra_cancel_clicked called with self.%s" % widget.get_name()
		self.quit()
	#-- FrmDlEsborra.on_bt_dl_esborra_cancel_clicked }

	#-- FrmDlEsborra.on_bt_dl_dacord_clicked {
	def on_bt_dl_dacord_clicked(self, widget, *args):
		print "on_bt_dl_dacord_clicked called with self.%s" % widget.get_name()
		self.esborra = True
		self.quit()
	#-- FrmDlEsborra.on_bt_dl_dacord_clicked }

