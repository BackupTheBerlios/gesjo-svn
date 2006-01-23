#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Imprimir
# 



class Informes:
	
	import reportlab 
	from reportlab.pdfgen import canvas 
	from reportlab.lib.pagesizes import cm, A4
	import reportlab.rl_config
	reportlab.rl_config.warnOnMissingFontGlyphs = 0
	from reportlab.pdfbase import pdfmetrics
	from reportlab.pdfbase.ttfonts import TTFont
	from reportlab.lib.fonts import addMapping
	
	
	
	
	def crea(self,fitxer,x=0,y=0):
		if x==0 and y==0:
			llarg,ample = self.A4
			
		else:
		
			llarg = y*self.cm
			ample = x*self.cm
		print ample, llarg
		c =self. canvas.Canvas("imprimir/"+fitxer,(ample,llarg),bottomup=0)
		c.translate(self.cm,self.cm)
		self.pdfmetrics.registerFont(self.TTFont("Nostra", "Times_New_Roman.ttf"))
	
		return c
		
	def pinta_logo(self,r):
		r.setFont("Nostra",12)
		r.drawString(0.1*self.cm,0.4*self.cm,"JOIERIA I RELLOTGERIA")
		r.setFont("Nostra",14)
		r.drawString(0.1*self.cm,1*self.cm,"BONNIN")
		r.setFont("Nostra",10)
		r.drawString(0.1*self.cm,1.5*self.cm,"Carrer Antoni Maura, 22")
		r.drawString(0.1*self.cm,2*self.cm,str("07460 Pollença - Espanya"))
		r.drawString(0.1*self.cm,2.5*self.cm,"tel. 971-533-716")
		r.drawString(0.1*self.cm,3*self.cm,"email. info@largenteria.com")
		r.line(0.1*self.cm,3.5*self.cm,9*self.cm,3.5*self.cm)
	
	def pinta_num_ticket(self,r,num):
		r.setFont("Nostra",16)
		r.drawString(6.5*self.cm,0.1*self.cm,"Nº- "+num)
		
	
	def pinta_id_client(self,r,num):
		r.setFont("Nostra",12)
		r.drawString(6.8*self.cm,1*self.cm,"CLIENT")
		r.setFont("Nostra",16)
		r.drawString(7.1*self.cm,1.5*self.cm,num)
	
	def pinta_data_entrada(self,r,data):
		r.setFont("Nostra",12)
		r.drawString(6.5*self.cm,2.5*self.cm,"Data d'entrada")
		r.setFont("Nostra",14)
		r.drawString(6.5*self.cm,3*self.cm,data)
		
	def pinta_marca(self,r, marca):
		r.setFont("Nostra",12)
		r.drawString(0.1*self.cm,4.2*self.cm,"Marca: ")
		r.setFont("Nostra",12)
		r.drawString(1.5*self.cm,4.2*self.cm,marca)
	
	def pinta_model(self,r, model):
		r.setFont("Nostra",12)
		r.drawString(0.1*self.cm,4.7*self.cm,"Model: ")
		r.setFont("Nostra",12)
		r.drawString(1.5*self.cm,4.7*self.cm,model)
		
		
	def pinta_det(self,r, gra,kts):
		r.setFont("Nostra",12)
		r.drawString(0.1*self.cm,5.2*self.cm,"Detalls:")
		r.setFont("Nostra",12)
		r.drawString(0.5*self.cm,5.7*self.cm,"gra: ")
		r.setFont("Nostra",12)
		r.drawString(3.7*self.cm,5.7*self.cm,"kts: ")
		r.setFont("Nostra",12)
		r.drawString(1.4*self.cm,5.7*self.cm,gra)
		r.drawString(4.5*self.cm,5.7*self.cm,kts)
		r.line(0.1*self.cm,6.1*self.cm,9*self.cm,6.1*self.cm)
		
	
	def pinta_treball(self,r, str):
		r.setFont("Nostra",10)
		r.drawString(0.1*self.cm,6.7*self.cm, "Treball:")
		r.setFont("Nostra",10)
		
		txt =r.beginText(0.5*self.cm,7.1*self.cm)
		print "provam...",str
		i = 0
		x,y = 0,1
		while i<len(str):
			txt.textLine(str[x*40:y*40])
			i +=40
			x +=1
			y+=1
		r.drawText(txt)
		
	
	
	def pinta_preu(self,r,preu):
		print preu
		if (preu=="None"):
			preu=" "
		r.line(0.1*self.cm,12*self.cm,9*self.cm,12*self.cm)
		r.setFont("Nostra",14)
		r.drawString(0.1*self.cm,12.5*self.cm,"Preu:")
		r.setFont("Nostra",14)
		r.drawString(2*self.cm,12.5*self.cm, preu+" €")
		
	def pinta_caduca(self,r):
		r.line(0.1*self.cm,12.8*self.cm,9*self.cm,12.8*self.cm)
		r.setFont("Nostra",12)
		r.drawString(3.2*self.cm,13.3*self.cm,"Caduca als 3 mesos")
		
	

	def canvi_pagina(self,r):
		r.showPage()
		
#~ ----------------------------------------------------------------------------------------------------------------------------------------------------
#~ Llistat d'arreglos
#~ ----------------------------------------------------------------------------------------------------------------------------------------------------

	def cap_pagina(self,r, titol,pagina):
		r.setFont("Nostra",10)
		
		r.drawString(1.1*self.cm,2*self.cm,titol)
		r.drawString(23.5*self.cm,2*self.cm,"Pàgina "+pagina)
		
		r.line(1*self.cm,2.2*self.cm,25*self.cm,2.2*self.cm)
		
	def linia(self,r,num,text):
		r.setFont("Nostra",10)
		r.drawString(1*self.cm,4*self.cm+num*0.5,text)
		
	def cap_arreglo(self,r,cols):
		r.setFont("Nostra",12)
		r.line(1*self.cm,3.7*self.cm,25*self.cm,3.7*self.cm)
		r.drawString(1*self.cm,3.6*self.cm,cols)
		
	
