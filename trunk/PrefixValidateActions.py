#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Autor: Josep Torrens Amer
# E-mail: toram74@gmail.com
#
# GNU GPL Licence, (C) 2005.
#
# Module: ValidarAccions
#
# Description: Classe d'ajuda per validar les entrades dels usuaris. 
# Vàlida els camps dels formularis.
#
# Version: 0.1
# 
# Created: 17-12-2005
#
# Modified:17-12-2005
#

import time
import gobject
import gtk

class PrefixValidateActions(gobject.GObject):
	__gsignals__ = {
		"mandatory-added" : ( gobject.SIGNAL_RUN_FIRST, None, (gtk.Widget,) ),
		"error-status"	: ( gobject.SIGNAL_RUN_FIRST, None, (gtk.Widget, bool) )
	}

	def __init__(self):
		gobject.GObject.__init__(self)
		self.mandatories = []

	def prefix_name(self, widget):
		def validate(widget):
			text = widget.get_text()
			error = len(text) < 1 or len(text) > 16
			self.emit("error-status", widget, error)
			
		def complete(widget, event):
			text = widget.get_text()
			cap = lambda s: s.capitalize()
			tokens = text.split()
			tokens = map(cap, tokens)
			text = " ".join(tokens)
			widget.set_text(text)

	widget.connect("changed", validate)
	widget.connect("focus-out-event", complete)

	def prefix_m(self, widget):
		self.add_mandatory(widget)

	def prefix_date(self, widget):
		def parse_date(text):
			(cY,cm,cd) = time.localtime()[0:3]
			try:
				(d,) = time.strptime(text, "%d")[2:3]
				m,Y = cm,cY
			except ValueError:
				try:
					(m,d) = time.strptime(text, "%d-%m")[1:3]
					Y = cY
				except:
					(Y,m,d) = time.strptime(text, "%d-%m-%y")[0:3]
			return (Y,m,d)
		
		def validate(widget):
			text = widget.get_text()
			try:
				parse_date(text)
				error = False
			except ValueError:
				error = True
			self.emit("error-status", widget, error)
		
		def complete(widget, event):
			text = widget.get_text()
			try:
				(Y,m,d) = parse_date(text)
				text = "%02d-%02d-%d" % (d,m,Y)
				widget.set_text(text)
				error = False
			except ValueError:
				error = True
			self.emit("error-status", widget, error)
		widget.connect("changed", validate)
		widget.connect("focus-out-event", complete)

	def prefix_age(self, widget):
		def validate(widget):
			text = widget.get_text()
			try:
				age = int(text)
				if age < 16 or age > 99:
					raise ValueError
				error = False
			except ValueError:
				error = True
			self.emit("error-status", widget, error)
		widget.connect("changed", validate)

	def prefix_cash(self, widget):
		def validate(widget):
			text = widget.get_text()
			try:
				cash = float(text)
				if cash < 0:
					raise ValueError
				error = False
			except ValueError:
				error = True
			self.emit("error-status", widget, error)
		widget.connect("changed", validate)

	def add_mandatory(self, widget):
		self.mandatories.append(widget)
		self.emit("mandatory-added", widget)

gobject.type_register(PrefixValidateActions)
