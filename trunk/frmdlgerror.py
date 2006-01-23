#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Autor: Josep Torrens Amer
# E-mail: toram74@gmail.com
#
# GNU GPL Licence, (C) 2005.
#
# Module: dlgerror
#
# Description: Modul de diàlegs d'errors
# Version: 0.0.1
# 
# Created: 28-12-2005
#
# Modified:28-12-2005
#

import os

import gtk


from appbase import AppBase

class FrmDlgError(AppBase):

	def __init__(self, gjlib):
		
		AppBase.__init__(self, gjlib, root="dlgError")

	def new(self):
		print "A new %s has been created" % self.__class__.__name__


	
	def run(self):
		self.show_form()
		
		AppBase.run( self )
		
		self.hide_form()
	
	


	

	
	def on_dlg_error_dacord_clicked(self, widget, *args):
		self.quit()
	

