#!/usr/bin/env python
# -*- coding: utf-8 -*-

import basedades
import ww
import datetime

class GJLib:
	""" Llibreria de funcions per Gesjo """
	def __init__(self,bd):
		self.reg_actual = {} # registres actuals de les fitxes, (clients, arreglos, ...)
		self.fitxaSQL = {}
		self.SQLINS = {}
		self.SQLBOR = {}
		self.SQLMOD = {}
		
		self.taules = {}
		self.camps = {}
		self.tipcamps = {}
		self.generadors = {}
		self.con = bd.con
		self.bd = bd
		
		# Iniciam estructures de dades de clients
		#
		self.fitxaSQL["cl"] = basedades.SQL(bd)
		self.fitxaSQL["ma"] = basedades.SQL(bd)
		self.fitxaSQL["ta"] = basedades.SQL(bd)
		self.fitxaSQL["me"] = basedades.SQL(bd)
		self.fitxaSQL["ar"] = basedades.SQL(bd)
		self.fitxaSQL["fa"] = basedades.SQL(bd)
		
		self.fitxaSQL["in"] = basedades.SQL(bd)
		
		
		self.fitxaSQL["cl"].executa("select * from client order by id")
		self.fitxaSQL["ma"].executa("select * from marca order by id")
		self.fitxaSQL["ta"].executa("select * from taller order by id")
		self.fitxaSQL["me"].executa("select * from mecanic order by id")
		self.fitxaSQL["ar"].executa("select * from arreglo order by id")
		self.fitxaSQL["fa"].executa("select * from factura order by id")
		
	
		self.anam_registre_primer("cl")
		self.anam_registre_primer("ma")
		self.anam_registre_primer("ta")
		self.anam_registre_primer("me")
		self.anam_registre_primer("ar")
		self.anam_registre_primer("fa")
		
		self.SQLINS["cl"] = basedades.SQL(bd)
		self.SQLINS["ma"] = basedades.SQL(bd)
		self.SQLINS["ta"] = basedades.SQL(bd)
		self.SQLINS["me"] = basedades.SQL(bd)
		self.SQLINS["ar"] = basedades.SQL(bd)
		self.SQLINS["fa"] = basedades.SQL(bd)
		
		self.SQLBOR["cl"] = basedades.SQL(bd)
		self.SQLBOR["ma"] = basedades.SQL(bd)
		self.SQLBOR["ta"] = basedades.SQL(bd)
		self.SQLBOR["me"] = basedades.SQL(bd)
		self.SQLBOR["ar"] = basedades.SQL(bd)
		self.SQLBOR["fa"] = basedades.SQL(bd)
		
		self.SQLMOD["cl"] = basedades.SQL(bd)
		self.SQLMOD["ma"] = basedades.SQL(bd)
		self.SQLMOD["ta"] = basedades.SQL(bd)
		self.SQLMOD["me"] = basedades.SQL(bd)
		self.SQLMOD["ar"] = basedades.SQL(bd)
		self.SQLMOD["fa"] = basedades.SQL(bd)
				
		
		self.taules["cl"] = "CLIENT"
		self.taules["ma"] = "MARCA"
		self.taules["ta"] = "TALLER"
		self.taules["me"] = "MECANIC"
		self.taules["ar"] = "ARREGLO"
		self.taules["fa"] = "FACTURA"
		
		#~ self.camps["cl"]=( "ID","NOM","LLINATGES","DIRECCIO1","DIRECCIO2", "POBLACIO","CODIPOSTAL", "TELEFON", "MOBIL", "EMAIL", "NOTES", "PAIS")
		#~ self.camps["ma"]=( "ID","NOM","DIRECCIO1","DIRECCIO2", "POBLACIO","CODIPOSTAL", "TELEFON", "FAX", "EMAIL", "NOTES", "PAIS")
		
	def ret_bd(self):
		"""
		Retorna el BD
		"""
		return self.bd
	
	def cancela(self,fitxa):
		self.fitxaSQL[fitxa].cancela()
		
		
	def ret_fitxa(self,fitxa):
		""" Mostra a la fitxa donada (clients, arreglos,...) el registre triat per reg 
		"""
		return (self.fitxaSQL[fitxa].ret_reg())
			
		
	def anam_registre_primer(self,fitxa):
		
		self.fitxaSQL[fitxa].primer_reg()
		self.reg_actual[fitxa] = self.fitxaSQL[fitxa].registre_actual()
		return True
	
	def anam_registre_darrer(self,fitxa):
		self.fitxaSQL[fitxa].darrer_reg()
		self.reg_actual[fitxa] = self.fitxaSQL[fitxa].registre_actual()
		return True
		
	
	def anam_registre_anterior(self, fitxa):
		self.fitxaSQL[fitxa].ant_reg()
		self.reg_actual[fitxa] = self.fitxaSQL[fitxa].registre_actual()
		return True
		
	def anam_registre_seguent(self, fitxa):
		
		self.fitxaSQL[fitxa].seg_reg()
		self.reg_actual[fitxa] = self.fitxaSQL[fitxa].registre_actual()
		return True
		

	def anam_fitxa(self,fitxa,pos):
		
		self.fitxaSQL[fitxa].anar_reg(pos)
		self.reg_actual[fitxa] = self.fitxaSQL[fitxa].registre_actual()
		return True
		
	def numero_fitxes(self, fitxa):
		"""
		Retorna el numero de registres
		que hi ha per fitxa
		"""
		return self.fitxaSQL[fitxa].numreg()


	def anam_registre(self,fitxa,reg):
		""" Ens situam al registre donat, nomes es una variable que guarda
		el numero de registre actual """
		print "anam a %d de la fitxa %s" % (reg, fitxa)
		self.reg_actual[fitxa] = reg
		
	def registre_actual(self, fitxa):
		""" Retorna el numero de registre actual per la fitxa donada """
		return self.reg_actual[fitxa]
		
	
	def modifica_fitxa(self, fitxa, valors):
		""" MODIFICA/Actualitza una fitxa """
	
		idv = valors[fitxa+"_id"] # guardam valor del ID
		del valors[fitxa+"_id"] # el treim de la llista
		
		cam = map(lambda x: x[3:].upper(), valors.keys())		
		va = []
		for k,v in zip(cam,valors.values()):
                    

                    if v=="":
                        continue
                            
                    print "------>",k,v
                    if k.endswith("_fl"):
                        va.append("%s = %s" % (k, str(float(v))))
                    else:
			print "K...",k
                        if k.startswith("DATA_"):
                                            
                            d,m,a = v.split("/")
                            print "d..",d,m,a
                            va.append("%s = '%s'" % (k,datetime.date(int(a),int(m),int(d)) ))
                        else:
                            va.append("%s = '%s'" % (k,unicode(v).replace("'","~" )))
                                    
		vals = ",".join(va)
		sent = "UPDATE  %s  SET %s WHERE ID=%s" % (self.taules[fitxa], vals, idv)
	
		print "SQL ",sent
		self.SQLMOD[fitxa].sqlmod(sent)
		self.SQLMOD[fitxa].acepta()
		self.fitxaSQL[fitxa].executa("select * from %s order by id" % self.taules[fitxa])
	
	def inserta_fitxa(self, fitxa, valors):
		""" 
		INSERTA una fitxa 
		"""
		try:
			del valors[fitxa+"_id"] # treim ID, no el necessitam per insertar
		except:
			pass
		cam = map(lambda x: x[3:].lower(), valors.keys())
		camps = ",".join(cam)
		va = []
		ci = []
		for k,v in zip(cam,valors.values()):	
			if v=="":
				continue
			
			ci.append(k)
			if k.endswith("_fl"):
				va.append(str(float(v)))
			else:
                            if k.startswith("DATA_"):
                                            
                                d,m,a = v.split("/")
                                print "d..",d,m,a
                                va.append(datetime.date(int(a),int(m),int(d)) )
                            else:
                                va.append(str(unicode(v).replace("'","~" )))
                                
		print ci, "---",va
		cin = ",".join(ci)
		vals = []
		for v in va:
			try:
				v_i = float(v)
			except:
					v_i = "\'"+v+"\'" 
			vals.append(str(v_i))
			
		vals = ",".join(vals)
		sent = "INSERT INTO %s (%s) VALUES(%s)" % (self.taules[fitxa], cin,vals)
		
		self.SQLINS[fitxa].sqlmod(sent)
		self.SQLINS[fitxa].acepta()
		self.fitxaSQL[fitxa].executa("select * from %s order by id" % self.taules[fitxa])
	
	def borra_fitxa(self, fitxa, id):
		""" Borram la fitxa actual """
		sent = "DELETE FROM %s WHERE ID = %s" % (self.taules[fitxa], id)
		print sent, self.reg_actual[fitxa]
		res = self.SQLBOR[fitxa].sqlmod(sent)
		print res
		self.SQLBOR[fitxa].acepta()
		self.fitxaSQL[fitxa].executa("select * from %s order by id" % self.taules[fitxa])
		
	def cerca(self,fitxa, cmpcerc):
		""" Cerca el registre pels camps donats """
		idcerca = basedades.SQL(self.bd)
		query = []
		qry = ""
		print "Cercare....",fitxa, cmpcerc
		
		for s in cmpcerc.keys():
			
			if s=="id":
				query.append( " %s=%s "  % (s.upper(),cmpcerc[s]))
			else:
				query.append( " %s LIKE '%s' "  % (s.upper(),cmpcerc[s]))
		
		qry = " and ".join(query)
		
		sent = "SELECT ID FROM %s WHERE %s" % (self.taules[fitxa], qry)
		
		print "Cercam...", sent
		idcerca.executa(sent)
		
		print idcerca.num_reg
		
		if idcerca.num_reg !=0:
			idcerca.primer_reg()
			ret = idcerca.ret_reg()['ID']
			pos = self.fitxaSQL[fitxa].troba_reg(ret)
			if pos != -1: # trobat
				self.anam_fitxa(fitxa,pos)
				return pos
			return None
		else:
			return None
			
	def fitxa_actual(self,fitxa):
		"""
			Retorna la posicio (index)
			de la fitxa actual 
		"""
		print fitxa
		print self.reg_actual[fitxa]
		return self.reg_actual[fitxa]
