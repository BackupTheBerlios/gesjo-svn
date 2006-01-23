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
import CampsCerc

class FrmLlistaTicket:
	
	
	def __init__(self, pIdClient, gjlib ):
		self.IDCLIENT = pIdClient
		self.bd = gjlib.ret_bd()
		self.gjlib= gjlib
		camps = CampsCerc()
		camps.posa_camp( "ID", int, "Codi", False )
		camps.posa_camp( "DATA", str, "Data", False )
		camps.posa_camp( "MODEL", str, "Model", False )
		camps.posa_camp( "MARCA", str, "Marca", False )
		camps.posa_camp( "TREBALL", str, "Treball", False )
		camps.posa_camp( "PVP", int, "PVP", False)
		self.c = camps
		
		
	def run(self):
		"""
		Executa la cerca
		"""
		sql = "SELECT ID, DATA, MODEL, MARCA, TREBALL, PVP FROM ARREGLOS WHERE CLIENT_ID=%s AND (ESTAT <>  'Facturat')" % self.IDCLIENT
		cur = self.bd.cursor()
		cur.execute( sql )
		dades = cur.fetchall()
			
		if DEBUG:  print dades
	
		frm_cerca = FrmCerca( self.c, dades, self.gjlib)
		return frm_cerca.run()