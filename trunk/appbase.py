#!/usr/bin/env python2.4
# -*- coding: utf-8 -*-
#
# Autor: Josep Torrens Amer
# E-mail: toram74@gmail.com
#
# GNU GPL Licence, (C) 2005.
#
# Module: frmmodul
#
# Description: Modul base
#
# Version: 0.0.1
# 
# Created: 19-12-2005
#
# Modified:19-12-2005
#

import os
import sys
import gtk
import datetime
import psycopg

from SimpleGladeApp import SimpleGladeApp
from SimpleGladeApp import bindtextdomain

app_name = "Gesjo"
app_version = "0.2.1"

glade_dir = "glade"
locale_dir = ""
glade_filename= "gesjo5.glade"

bindtextdomain(app_name, locale_dir)



class AppBase(SimpleGladeApp):
	
	def __init__( self,  gjlib, path=glade_filename, root=None, domain=app_name, **kwargs ):
		path = os.path.join(glade_dir, path)
		
		self.gjlib = gjlib
		self.edita = {}
		self.camps_editats = {}
		
		SimpleGladeApp.__init__(self, path, root, domain, **kwargs)
		
		

	def show_form(self):
		"""
		Show the main widget.
		Added by Josep Torrens
		"""
		self.main_widget.show()
		
	def hide_form(self):
		"""
		Hide the main widget.
		Added by Josep Torrens
		"""
		self.main_widget.hide()
		


	def editam_fitxa(self,fitxa):
		"""
		L'usuari edita una fitxa
		"""
		print "Editam ",fitxa

		self.edita[fitxa] = True

		self.get_widget('bt_'+fitxa+'_aplica').show()
		self.get_widget('bt_'+fitxa+'_cancel').show()
		if fitxa == "ar":
			self.bt_ar_cerc_client.set_sensitive( True )
			self.ar_estat.set_sensitive( True )
			self.bt_ar_cerca_dt_entrada.set_sensitive( True )
			self.bt_ar_cerca_dt_sortida.set_sensitive( True )
			self.bt_ar_cerca_dt_entrega.set_sensitive( True )
			self.bt_ar_cerca_dt_tornada.set_sensitive( True )
		
		if fitxa == "fa":
			self.bt_fa_cerc_client.set_sensitive( True )
			self.fa_estat_factura.set_sensitive( True )
			self.bt_fa_cerca_dt.set_sensitive( True )
			#self.bt_fa_inserta_ticket.set_sensitive( True )
			#self.bt_fa_inserta_linia.set_sensitive( True )
			self.bt_fa_elimina_linia.set_sensitive( True )
		
			
		self.memento_on(fitxa)

	def memento_on(self, fitxa, borra=False):
		"""
		Es guarden els valors de la fitxa per despres poder restaurar-los en cas de cancelar
		"""
		
		for x in self.glade.get_widget_prefix(fitxa+"_"):
			print "provam camp..",x.get_name()
			if x.get_name().endswith("_moff"):
				model = x.get_model()
				valors= []
				for g in model:
					linia= []
					for y in g:
						linia.append(y)
					valors.append(linia)

				self.camps_editats[ x.get_name() ] = valors
				if borra:
					x.get_model().clear()
				
				continue
					
			if type(x) is gtk.TextView:
				y =x.get_buffer()
				inici_iter, final_iter = y.get_bounds()
				self.camps_editats[ x.get_name() ] = y.get_text( inici_iter, final_iter )
				if borra:
					y.set_text("")
			else:
				if type(x) is gtk.ComboBox:
					self.camps_editats[ x.get_name() ] = x.get_active_text()
					
				else:
					self.camps_editats[ x.get_name() ] = x.get_text()
					if borra:
						x.set_text("")
					
			

	def memento_off(self, fitxa ):
		"""
		Restauram els valors de la fitxa abans guardats amb memento_on
		"""
		
		for x in  self.glade.get_widget_prefix( fitxa+"_" ):
			if x.get_name().endswith("_moff"):
				model = x.get_model()
				model.clear()
				llista = self.camps_editats[ x.get_name() ]
				for f in llista:
					print "F ",f
					model.append(f)
					
				continue 
					
			if type(x) is gtk.TextView:
				x.get_buffer().set_text( self.camps_editats[ x.get_name() ] )
			else:
				if type(x) is gtk.ComboBox:
					model = x.get_model()
					val = self.camps_editats[ x.get_name() ]
					if val is None:
						index = 0
					else:
						index = [ r[0] for r in model ].index( val )   
					x.set_active( index )
				else:
					x.set_text( self.camps_editats[x.get_name() ] )
				
			del self.camps_editats[ x.get_name() ]
		pass

		
	def nova_fitxa(self,fitxa):
		"""
		L'usuari fa una nova fitxa
		"""
		print "Nova fitxa"

		self.edita[fitxa] = False
		
		self.memento_on( fitxa, borra=True )
		
		self.get_widget('bt_'+fitxa+'_aplica').show()
		self.get_widget('bt_'+fitxa+'_cancel').show()
		
		if fitxa == "ar":
			self.bt_ar_cerc_client.set_sensitive(True)
			self.bt_ar_cerca_dt_entrada.set_sensitive( True )
			self.bt_ar_cerca_dt_sortida.set_sensitive( True )
			self.bt_ar_cerca_dt_entrega.set_sensitive( True )
			self.bt_ar_cerca_dt_tornada.set_sensitive( True )
			
			self.ar_estat.set_sensitive( True )
			self.ar_estat.set_active(0)
			self.ar_data_entrada.set_text(datetime.date.today().strftime("%d-%m-%y") )
			self.bt_ar_cerc_client.set_sensitive( True )

		if fitxa == "fa":
			self.bt_fa_cerc_client.set_sensitive( True )
			self.fa_estat_factura.set_sensitive( True )
			self.fa_estat_factura.set_active(0)
			self.bt_fa_cerca_dt.set_sensitive( True )
			#self.bt_fa_inserta_ticket.set_sensitive( True )
			#self.bt_fa_inserta_linia.set_sensitive( True )
			self.bt_fa_elimina_linia.set_sensitive( True )
		




		try:
			if ( self.get_widget(fitxa+"_nom") ):
				self.get_widget(fitxa+"_nom").grab_focus()
		except:
			pass
			
	def cancelam_fitxa(self,fitxa):
		"""
		L'usuari cancela l'entrada o
		modificacio de la fitxa
		"""
		print "Cancelam nou/edicio ",fitxa
		self.get_widget('bt_'+fitxa+'_aplica').hide()
		self.get_widget('bt_'+fitxa+'_cancel').hide()
		
		if fitxa == "ar":
			self.bt_ar_cerc_client.set_sensitive( False )
			
			self.bt_ar_cerca_dt_entrada.set_sensitive( False )
			self.bt_ar_cerca_dt_sortida.set_sensitive( False)
			self.bt_ar_cerca_dt_entrega.set_sensitive( False )
			self.bt_ar_cerca_dt_tornada.set_sensitive( False)
			
			self.ar_estat.set_sensitive( False )
			
			self.bt_ar_cerc_client.set_sensitive( False )
		
		if fitxa == "fa":
			self.bt_fa_cerc_client.set_sensitive( False )
			self.fa_estat_factura.set_sensitive( False )

			self.bt_fa_cerca_dt.set_sensitive( False )
			#self.bt_fa_inserta_ticket.set_sensitive( False )
			#self.bt_fa_inserta_linia.set_sensitive( False )
			self.bt_fa_elimina_linia.set_sensitive( False )
		
		
		
		self.memento_off( fitxa ) 
		
		self.edita[fitxa] = False

		


	def aceptam_fitxa(self,fitxa):
		"""
		L'usuari acepta/valida
		l'entrada o modificacio de
		la fitxa
		"""
		print "Aceptam nou/edicio ",fitxa

		fit = {}

		for x in self.glade.get_widget_prefix(fitxa+"_"):
			if x.get_name().endswith("_calc"):
				continue
			if x.get_name().endswith("_moff"):
				continue
			if type(x) is gtk.TextView:
				y =x.get_buffer()
				inici_iter, final_iter = y.get_bounds()
				fit[x.get_name()]=y.get_text(inici_iter,final_iter)
			else:
				if type(x) is gtk.ComboBox:
					fit[x.get_name() ] =  x.get_active_text()
				else:
					fit[ x.get_name() ] = x.get_text()


		print "fitxa..."
		print fit
		try:
			if (self.edita[fitxa]):
				self.gjlib.modifica_fitxa(fitxa,fit)
				#if fitxa==""fa":
				self.	
			else:
				self.gjlib.inserta_fitxa(fitxa,fit)
				
			for x in ( self.glade.get_widget_prefix( fitxa+"_" ) ):
				if type(x) in (gtk.Entry,gtk.ComboBox,gtk.TextView):
					del self.camps_editats[x.get_name()]
		
			self.get_widget('bt_'+fitxa+'_aplica').hide()
			self.get_widget('bt_'+fitxa+'_cancel').hide()
			if fitxa == "ar":
				self.bt_ar_cerc_client.set_sensitive( False )
		
				self.bt_ar_cerca_dt_entrada.set_sensitive( False )
				self.bt_ar_cerca_dt_sortida.set_sensitive( False)
				self.bt_ar_cerca_dt_entrega.set_sensitive( False )
				self.bt_ar_cerca_dt_tornada.set_sensitive( False)
				
				self.ar_estat.set_sensitive( False )
				self.bt_ar_cerc_client.set_sensitive( False )
			
			
			if fitxa == "fa":
				self.bt_fa_cerc_client.set_sensitive( False )
				self.fa_estat_factura.set_sensitive( False )
				
				self.bt_fa_cerca_dt.set_sensitive( False )
			
			self.edita[fitxa] = False
		except (psycopg.Error,psycopg.ProgrammingError), detail:
			import frmdlgerror
			frm_dlg = frmdlgerror.FrmDlgError( self.gjlib )
			infoerror = frm_dlg.get_widget("dl_error_msg")
			infoerror.set_markup("<b>Error:</b> %s" % detail)
			frm_dlg.run()
			
			self.gjlib.cancela(fitxa)

	
	def esborra_fitxa(self,fitxa):
		""" 
		L'usuari esborra una fitxa
		"""
		print "Esborra fitxa"
		import frmdlgesborra
		frm_dlg = frmdlgesborra.FrmDlEsborra( self.gjlib )
		info = frm_dlg.get_widget("dl_esborra")
		if fitxa == "cl": 
			tipus = "el client"
		if fitxa == "ar":
			tipus = "l'arreglo"
		if fitxa == "me":
			tipus = "el mecànic"
		if fitxa == "ma":
			tipus = "aquesta marca"
		if fitxa == "ta":
			tipus = "aquest taller"
			
		objecte = self.get_widget(fitxa+"_id").get_text()
		nom = self.get_widget(fitxa+"_nom")
		if nom:
			objecte += " (%s)" % nom.get_text()
		info.set_markup("<b>Segur que vols esborrar <big>%s %s</big> ? </b>" % (tipus, objecte) )
		
		rc = frm_dlg.run()
		print "Tria ",rc
		if (rc): 
			self.gjlib.borra_fitxa(fitxa,self.get_widget(fitxa+"_id").get_text())
			print "Fet"
			self.darrera_fitxa(fitxa)

	def primera_fitxa(self,fitxa):
		"""
		Anar a la primera fitxa
		"""
		print "Anam a la primera ",fitxa
		self.gjlib.anam_registre_primer(fitxa)
		self.mostra_fitxa(fitxa)
		print "som a %s..." % fitxa,self.gjlib.registre_actual(fitxa)

	def mostra_fitxa(self,fitxa):
			""" fica les dades del registre actual
			a la fitxa donada (del gui) """
			res = {}
			res = self.gjlib.ret_fitxa(fitxa)
			if res:
				print "mostram fitxa %s...." % fitxa
				print "...",res
				print ".........",res.keys()


				for cmp in map(str.lower,res.keys()):
					w = "%s_%s" % (fitxa, cmp)
					print "camp...",w
					cw = self.get_widget(w)
					
					v = ""
					
					# Miram si hi ha claus foranees
					if cmp.endswith( "_id" ):
						print "Hem trobat la clau foranea...",cmp
						taularef,codi = cmp.split("_")
						fitxaref = taularef[:2]
						cercam = {}
						# Si la clau no es nula, cercam el valor associat
						if res[cmp]:
							cercam["id"] = int(res[cmp])
							regcerc = self.gjlib.cerca(fitxaref,cercam)
							self.gjlib.anam_fitxa(fitxaref,regcerc)
							reg = self.gjlib.ret_fitxa(fitxaref)
							print "%s_%s" % (fitxa, taularef)
							print "reg...",reg["nom"]
							w = self.get_widget("%s_%s_calc" % (fitxa, taularef))
							w.set_text(reg['nom'])
							
					if ( type( cw ) is gtk.TextView ):
						
						if res[cmp]==None:
							res[cmp] = ""	
						self.get_widget(w).get_buffer().set_text(res[cmp].replace("~","'"))
					else:
						
						if ( type( cw ) is gtk.ComboBox ):
							
							model = cw.get_model()
							val = res[cmp]
							if val is None:
								index = 0
							else:
								index = [ r[0] for r in model ].index( val )   
							cw.set_active( index )
						else:
							if not res[cmp]:
								v= ""
							else:
								if ( type( cmp ) is int):
										v = unicode( int( res[cmp] ) ).zfill( 5 )
								
								if ( type( cmp ) is str):
									v = unicode(str(res[cmp]).replace("~","'"))
									
								if ( cmp.startswith("data_") ):
									
									#any,mes,dia = str(res[cmp]).split("-")
									#v = "%s/%s/%s" % (dia,mes,any)
									v = res[cmp].strftime("%d/%m/%y")

									
								if ( cmp.endswith("_fl") ):
									print "miram si es grs-kts",cmp," i es...",res[cmp]
									v = unicode(float(res[cmp])).zfill(5)
			
							cw.set_text(v)

	def anterior_fitxa(self,fitxa):
		"""
		Anam a la fitxa anterior
		"""
		print "Anam a l'anterior ",fitxa
		self.gjlib.anam_registre_anterior(fitxa)
		self.mostra_fitxa(fitxa)
		print "som a %s..." % fitxa,self.gjlib.registre_actual(fitxa)

	def seguent_fitxa(self,fitxa):
		"""
		Anam a la fitxa següent
		"""
		print "Anam a la següent ", fitxa
		self.gjlib.anam_registre_seguent(fitxa)
		self.mostra_fitxa(fitxa)
		print "som a %s..." % fitxa,self.gjlib.registre_actual(fitxa)


	def darrera_fitxa(self, fitxa):
		"""
		Anam a la darrera fitxa
		"""
		print "Anam a la darrera ", fitxa
		self.gjlib.anam_registre_darrer(fitxa)
		self.mostra_fitxa(fitxa)
		print "som a %s..." % fitxa,self.gjlib.registre_actual(fitxa)

	def cerca_fitxa(self,fitxa):
		"""
		Cercam una fitxa
		"""
		print "Cercam fitxa de",fitxa
		
