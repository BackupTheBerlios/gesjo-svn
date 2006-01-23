#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Autor: Josep Torrens Amer
# E-mail: toram74@gmail.com
#
# GNU GPL Licence, (C) 2005.
#
# Module: dlgcerca
#
# Description: Modul de  diàleg de cercques
#
# Version: 0.0.1
# 
# Created: 19-12-2005
#
# Modified: 29-12-2005
#

import os

import gtk

from SimpleGladeApp import AppBase

class DlgCerca(AppBase):

	def __init__(self, gjlib ):
		AppBase.__init__(self, gjlib,  root="dlg_cerca")


	#-- DlgCerca.new {
	def new(self):
		print "A new %s has been created" % self.__class__.__name__
	#-- DlgCerca.new }

	#-- DlgCerca custom methods {

	#-- DlgCerca custom methods }


