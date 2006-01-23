#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Autor: Josep Torrens Amer
# E-mail: toram74@gmail.com
#
# GNU GPL Licence, (C) 2005.
#
# Module: frmcalendari
#
# Description: Modul de calendaris
#
# Version: 0.0.1
# 
# Created: 22-12-2005
#
# Modified:22-12-2005
#

import os

import gtk


from appbase import AppBase


class Frmcalendari(AppBase):

	def __init__(self, gjlib ):
		
		
##		self.data = None
		AppBase.__init__( self,  gjlib, root="dlgcalendari")
			
	#-- Frmcalendari.new {
	def new(self):
		print "A new %s has been created" % self.__class__.__name__
	#-- Frmcalendari.new }

	#-- Frmcalendari custom methods {
	
	def run(self):
		self.show_form()
		
		AppBase.run( self )
		
		self.hide_form()
		return self.calendari.get_date()
		
	#-- Frmcalendari custom methods }

	#-- Frmcalendari.on_calendar_day_selected_double_click {
	def on_calendar_day_selected_double_click(self, widget, *args):
		print "on_calendar_day_selected_double_click called with self.%s" % widget.get_name()
		self.quit()
	#-- Frmcalendari.on_calendar_day_selected_double_click }

