#!/usr/bin/env python
# -*- coding: utf-8 -*-


import db_row
# from  kinterbasdb import typeconv_fixed_fixedpoint as tfi
# from kinterbasdb import typeconv_text_unicode as ttu

class SQL:
	""" Classe SQL, son objectes de les sentencies SQL (+- com els cursors) 
	"""
	
	def __init__(self, basedad):
		""" con: conexio a la BD """
		self.bd = basedad
		self.conexio = self.bd.con
		self.sentencia = ""
		self.num_reg = 0
		self.reg_actual = 0
		self.camps = []
		self.cur = None
		
	def cancela(self):
		self.conexio.rollback()
	
	def acepta(self):
		self.conexio.commit()
		
	
	def executa(self,sent=""):
		""" executa la sentencia (sent) passada """
		if  (not self.conexio) or (sent == ""):
			return FALSE
		
		#
		# Començam, declaram cursor
		#
		self.cur = self.conexio.cursor() 
		
		# executam sentencia
		self.sentencia = sent
		
		print "Executam...",sent
		self.cur.execute(self.sentencia)
		
		
		#Extraim noms dels camps 
		self.camps = list(map(lambda x: x[0].lower(),self.cur.description))
		
		#Normalitzam a miniscules i el charset
		self.camps2 = []
		for cmp in self.camps:
			try:
				self.camps2.append(cmp.decode('utf8'))
			except ValueError:
				self.camps2.append(cmp.decode('iso8859-15'))
		
		self.camps = self.camps2
				
		
		self.R =  db_row.IMetaRow(self.cur.description)
		
		self.results = [ self.R(row) for row in self.cur.fetchall() ]
		
		# Num de registres retornats
		self.num_reg = len(self.results)
		
		return True
		
	def sqlmod(self, sent,va=[]):
		""" sqls per modificar, insertar o borrar """
		if  (not self.conexio) or (sent == ""):
			return FALSE
		
		#
		# Començam, declaram cursor
		#
		self.cur = self.conexio.cursor() 
		
		# executam sentencia
		
		print type(sent)
		print "Provam....",sent
		print "...i ara...",str(sent).encode('latin1')
		
		
		if va!=[]:
			self.cur.execute(sent,va)
		else:
			#~ self.cur.execute(sent)
			self.cur.execute(str(sent).encode('utf8'))

			
		print "Fet "
		self.num_reg = 0
		
	def primer_reg(self):
		self.reg_actual = 0
	
	def darrer_reg(self):
		self.reg_actual = self.num_reg-1
		
	def numreg(self):
		return self.num_reg
	
	def registre_actual(self):
		return self.reg_actual
		
	def ret_reg(self):
		if self.num_reg >0:
			return self.results[self.reg_actual]
		else:
			return None
		
	def anar_reg(self,reg):
		if (reg >= 0) and (reg < self.num_reg):
			self.reg_actual = reg
	
	def seg_reg(self):
		if (self.reg_actual+1 < self.num_reg):
			self.reg_actual += 1
		else:
			self.reg_actual = self.num_reg-1
			
	def ant_reg(self):
		if (self.reg_actual-1>=0):
			self.reg_actual -= 1
		else:
			self.reg_actual = 0
	
	def troba_reg(self,idc):
		""" cerca quin registre te el ID donat """
		i = 0
		for x in self.results:
			if x.dict()['id'] ==idc:
				return i
			i += 1
		return -1
		
class BaseDades:
	""" Clase encapçuladora de la base de dades"""
	import  psycopg as bdd
	
	
	
	def __init__(self):
		self.con = None
		
	
	def connexio(self,base="basededades",usuari="bda",clau="bdaclau", port="5432"):
		print "Intentam conectar a la BD %s  amb l'usuari %s " % (base, usuari)
		dsn = "dbname=%s user=%s password=%s port=%s " % ( base, usuari, clau, port )
		try:
			self.con = self.bdd.connect( dsn )
		except self.bdd.OperationalError:
			print "No s'ha pogut conectar a la BD" 
			
		if (self.con):
			return True
		else:
			return False

	def desconnexio(self):
		if (self.con):
			self.con.disconnect()
	
	def cursor(self):
		if (self.con):
			return self.con.cursor()
		else:
			return None

