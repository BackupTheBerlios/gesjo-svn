#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Autor: Josep Torrens Amer
# E-mail: toram74@gmail.com
#
# GNU GPL Licence, (C) 2005.
#
# Module: frmbrowse
#
# Description: Modul de navegació de les fitxes
#
# Version: 0.0.1
# 
# Created: 19-12-2005
#
# Modified:19-12-2005
#

import os

import gtk

from SimpleGladeApp import AppBase
from SimpleGladeApp import bindtextdomain

app_name = "Gesjo"
app_version = "0.2.1"

glade_dir = "glade"
locale_dir = ""

bindtextdomain(app_name, locale_dir)

class Frmbrowse(AppBase):

	def __init__(self, path="gesjo5.glade",
				 root="frmbrowse",
				 domain=app_name, **kwargs):
		path = os.path.join(glade_dir, path)
		AppBase.__init__(self, path, root, domain, **kwargs)

	#-- Frmbrowse.new {
	def new(self):
		print "A new %s has been created" % self.__class__.__name__
	#-- Frmbrowse.new }

	#-- Frmbrowse custom methods {
	#   Write your own methods here
	#-- Frmbrowse custom methods }

	#-- Frmbrowse.on_brw_select_cursor_row {
	def on_brw_select_cursor_row(self, widget, *args):
		print "on_brw_select_cursor_row called with self.%s" % widget.get_name()
	#-- Frmbrowse.on_brw_select_cursor_row }

	#-- Frmbrowse.on_bt_ta_primer_clicked {
	def on_bt_ta_primer_clicked(self, widget, *args):
		print "on_bt_ta_primer_clicked called with self.%s" % widget.get_name()
	#-- Frmbrowse.on_bt_ta_primer_clicked }

	#-- Frmbrowse.on_bt_ta_anterior_clicked {
	def on_bt_ta_anterior_clicked(self, widget, *args):
		print "on_bt_ta_anterior_clicked called with self.%s" % widget.get_name()
	#-- Frmbrowse.on_bt_ta_anterior_clicked }

	#-- Frmbrowse.on_bt_ta_seguent_clicked {
	def on_bt_ta_seguent_clicked(self, widget, *args):
		print "on_bt_ta_seguent_clicked called with self.%s" % widget.get_name()
	#-- Frmbrowse.on_bt_ta_seguent_clicked }

	#-- Frmbrowse.on_bt_ta_darrer_clicked {
	def on_bt_ta_darrer_clicked(self, widget, *args):
		print "on_bt_ta_darrer_clicked called with self.%s" % widget.get_name()
	#-- Frmbrowse.on_bt_ta_darrer_clicked }

	#-- Frmbrowse.on_bt_sel_si_clicked {
	def on_bt_sel_si_clicked(self, widget, *args):
		print "on_bt_sel_si_clicked called with self.%s" % widget.get_name()
	#-- Frmbrowse.on_bt_sel_si_clicked }

	#-- Frmbrowse.on_bt_sel_cancel_clicked {
	def on_bt_sel_cancel_clicked(self, widget, *args):
		print "on_bt_sel_cancel_clicked called with self.%s" % widget.get_name()
	#-- Frmbrowse.on_bt_sel_cancel_clicked }

