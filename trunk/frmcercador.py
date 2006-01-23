#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Autor: Josep Torrens Amer
# E-mail: toram74@gmail.com
#
# GNU GPL Licence, (C) 2005.
#
# Module: frmCercador
#
# Description: Modul de gestió de cerques 
#
# Version: 0.0.1
# 
# Created: 29-12-2005
#
# Modified:29-12-2005
#



import gtk
from frmrecercador import Frmrecercador
from frmcerca import FrmCerca

DEBUG = 1

class FrmCercador:
	"""
	Classe que crea els dialegs per cercar una fitxa a una taula
	"""

	def __init__(self, pCamps, pTaula, gjlib ):
		self.c = pCamps
		self.bd = gjlib.ret_bd()
		self.t = pTaula
		self.gjlib= gjlib
		
		
	def run(self):
		"""
		Executa la cerca
		"""
		frm_cercador = Frmrecercador( self.c, self.gjlib )
		cercar = frm_cercador.run()

		if cercar:
			sql = "SELECT "+ ",".join(self.c.obte_camps())+" FROM "+self.t
			if  cercar:
				sql += " WHERE " + " and  ".join(["%s LIKE '#%s#'" % (k, v) for k, v in cercar.items() if (v != "")])
				sql = sql.replace("#","%")
		
			if DEBUG: print "SQL: "+sql
			cur = self.bd.cursor()
			cur.execute( sql )
			dades = cur.fetchall()
			
			if DEBUG:  print dades
		
			frm_cerca = FrmCerca( self.c, dades, self.gjlib)
			return frm_cerca.run()
			
 


