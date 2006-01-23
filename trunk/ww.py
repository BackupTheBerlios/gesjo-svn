#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Classe del GUI
# 

import gtk
import types
import new
import gobject
import informes 
import datetime as data
import sys
import os
import frmmarca
import frmtaller
import frmmecanic
import frmcalendari
import frmcercador
from CampsCerc import CampsCerc
from frmllistticket import FrmLlistaTicket


from appbase import AppBase

class WidApp(AppBase):
	def __init__( self,  gjlib):
				
		AppBase.__init__(self, gjlib, root="frmgesjo")
	
	def new(self):
		
		self.frmmarca = frmmarca.Frmmarca( self.gjlib )
		self.frmtaller = frmtaller.Frmtaller( self.gjlib )
		self.frmmecanic = frmmecanic.Frmmecanic( self.gjlib )
		self.frmcalendari = frmcalendari.Frmcalendari( self.gjlib )
		self.camps_cercar = []
		self.valors_cercar = []



		# eliminam les petanyes de la dreta
		self.pestanya.set_show_tabs( False )


		#
		#
		#Pestanya
		#
		# FACTURES
		#
		#
		# establim les columnes/camps del model i el cream  
		self.fa_liststore = gtk.ListStore( str, float, float, float )
		self.fa_linies_moff.set_model(self.fa_liststore)

		# anem a crear les columnes, ;)
		
		#descripcio
		self.cell = gtk.CellRendererText()
		self.cell.set_property('editable', True)
		self.cell.set_property('editable-set', True)

		self.tvcolumn = gtk.TreeViewColumn("Descripció", self.cell, text=0)
		self.tvcolumn.set_min_width(400)
		
		self.fa_linies_moff.append_column(self.tvcolumn)
		
		#preu
		self.cell = gtk.CellRendererText()
		self.cell.set_property('editable', True)
		self.cell.set_property('editable-set', True)
		
		self.tvcolumn = gtk.TreeViewColumn("Preu", self.cell, text=1)
		self.tvcolumn.set_min_width(80)
		self.fa_linies_moff.append_column(self.tvcolumn)
		
		#unitats
		self.cell = gtk.CellRendererText()
		self.cell.set_property('editable', True)
		self.cell.set_property('editable-set', True)
		
		self.tvcolumn = gtk.TreeViewColumn("Unitats", self.cell, text=2)
		self.tvcolumn.set_min_width(80)
		self.fa_linies_moff.append_column(self.tvcolumn)
		
		self.cell = gtk.CellRendererText()
		self.cell.set_property('editable', True)
		self.cell.set_property('editable-set', True)
		
		self.tvcolumn = gtk.TreeViewColumn("Import", self.cell, text=3)
		self.tvcolumn.set_min_width(80)
		self.fa_linies_moff.append_column(self.tvcolumn)
		
		


	def on_btsurt_clicked(self,event):
		print "Sortint..."
		gtk.main_quit()
		sys.exit(0)

	def on_btfactures_clicked(self,event):
		print "Anam a factures"
		self.pestanya.set_current_page(2)
		self.mostra_fitxa("fa")



	def on_btarreglos_clicked(self,event):
		print "Anam a arreglos"
		self.pestanya.set_current_page(1)
		self.mostra_fitxa("ar")

	def on_btclients_clicked(self,event):
		print "Anam a clients"
		self.pestanya.set_current_page(0)		
		self.mostra_fitxa("cl")

	def on_btinformes_clicked(self,event):
		print "Anam a informes"
		self.pestanya.set_current_page(3)		


#~ ----------------------------------------------------------------------------------------------------------------------------------		
 #~ Events pels menus
 #~ ----------------------------------------------------------------------------------------------------------------------------------

	def on_mnsurt_activate(self,event):
		print "Sortint..."
		gtk.main_quit()
		sys.exit(0)

	def  on_mnmarques_activate_item(self,event):
		print "Manteniment de Marques"
		self.frmmarca.mostra_fitxa("ma")
		self.frmmarca.show_form()



	def on_mntallers_activate_item(self,event):
		print "Manteniment de Tallers"
		self.frmtaller.mostra_fitxa("ta")
		self.frmtaller.show_form()


	def on_mnmecanics_activate_item (self,event):
		print "Manteniment de Mecanics"
		self.frmmecanic.mostra_fitxa("me")
		self.frmmecanic.show_form()

	def on_bt_me_cerca_taller_clicked(self,event):
			pass


	def on_bt_in_ar_sobres_clicked(self,event):
		print  "AQUIII"


#------------------------------------------------------------------------------------------------------------------------------------------------------
# Funcions GENERIQUES
# d'us dels botons i demes
#-----------------------------------------------------------------------------------------------------------------------------------------------------

	def imprimir_ticket(self):
		"""
		Imprimeix el ticket donat
		"""
		inf = informes.Informes()

		reg = self.gj.ret_fitxa("ar")

		r = {}
		for x in reg.keys():
			try:
				r[x] = str(int(reg[x]))
			except:
				r[x] = str(reg[x])

		# cream pdf
		rpt = inf.crea("ticket_"+r["ID"]+".pdf",10,14.5)
		inf.pinta_logo(rpt)

		inf.pinta_num_ticket(rpt,r["ID"].zfill(5))

		inf.pinta_id_client(rpt,r["CLIENT_ID"].zfill(5))
		a,m,d = r["DATA_ENTRADA"].split("-")
		inf.pinta_data_entrada(rpt,"%s/%s/%s" % (d,m,a))

		inf.pinta_marca(rpt,r["MARCA"])
		inf.pinta_model(rpt,r["MODEL"])
		inf.pinta_treball(rpt,r["TREBALL"])
		inf.pinta_det(rpt,r["GRA_FL"],r["KTS_FL"])

		inf.pinta_preu(rpt,r["PVP"])
		inf.pinta_caduca(rpt)

		rpt.showPage()
		rpt.save()








	# 
	# ---------------------------------------------------------------------------------------------------------------------------------------------
	#
	# Events de CLIENTS
	#
	# ---------------------------------------------------------------------------------------------------------------------------------------------
	#

	def on_bt_cl_cancel_clicked(self,event):
		"""
		Cancela l'entrada de clients
		"""
		print "Cancelam nou/edicio client"
		self.cancelam_fitxa("cl")


	def on_bt_cl_aplica_clicked(self,event):
		"""
		Acepta l'entrada de clients
		"""
		print "Aceptam nou/edicio client"
		self.aceptam_fitxa("cl")

	def on_bt_cl_edita_clicked(self,event):
		"""
		Edita el client
		"""
		print "Editam client"
		self.editam_fitxa("cl")

	def on_bt_cl_nou_clicked(self,event):
		"""
		Entra un nou client
		"""
		print "Nou client"
		self.nova_fitxa("cl")

	def on_bt_cl_esborra_clicked(self,event):
		"""
		Esborra un client
		"""
		print "Esborra client"
		self.esborra_fitxa("cl")

	def on_bt_cl_primer_clicked(self,event):
		"""
		Anam al primer client
		"""
		self.primera_fitxa("cl")

	def on_bt_cl_anterior_clicked(self,event):
		"""
		Anam al client anterior
		"""
		self.anterior_fitxa("cl")

	def on_bt_cl_seguent_clicked(self,event):
		"""
		Anam al client següent
		"""
		self.seguent_fitxa("cl")

	def on_bt_cl_darrer_clicked(self, event):
		"""
		Anam al darrer client
		"""
		self.darrera_fitxa("cl")


	def on_bt_cl_cerca_clicked(self,event):
		"""
		Cercam un client
		"""
		#self.cerca_fitxa("cl")
	


    # 
	# ---------------------------------------------------------------------------------------------------------------------------------------------
	#
	# Events de TALLERS
	#
	# ---------------------------------------------------------------------------------------------------------------------------------------------
	#
	def on_bt_ta_cancel_clicked(self,event):
		"""
		Cancela l'entrada de tallers
		"""
		print "Cancelam nou/edicio taller"
		self.cancelam_fitxa("ta")


	def on_bt_ta_aplica_clicked(self,event):
		"""
		Acepta l'entrada de tallers
		"""
		print "Aceptam nou/edicio taller"
		self.aceptam_fitxa("ta")

	def on_bt_ta_edita_clicked(self,event):
		"""
		Edita el taller
		"""
		print "Editam taller"
		self.editam_fitxa("ta")

	def on_bt_ta_nou_clicked(self,event):
		"""
		Entra un nou taller
		"""
		print "Nou taller"
		self.nova_fitxa("ta")

	def on_bt_ta_esborra_clicked(self,event):
		"""
		Esborra un taller
		"""
		print "Esborra taller"
		self.esborra_fitxa("ta")

	def on_bt_ta_primer_clicked(self,event):
		"""
		Anam al primer taller
		"""
		self.primera_fitxa("ta")

	def on_bt_ta_anterior_clicked(self,event):
		"""
		Anam al taller anterior
		"""
		self.anterior_fitxa("ta")

	def on_bt_ta_seguent_clicked(self,event):
		"""
		Anam al taller següent
		"""
		self.seguent_fitxa("ta")

	def on_bt_ta_darrer_clicked(self, event):
		"""
		Anam al darrer taller
		"""
		self.darrera_fitxa("ta")


	def on_bt_ta_cerca_clicked(self,event):
		"""
		Cercam un taller
		"""
		self.cerca_fitxa("ta")


# 
	# ---------------------------------------------------------------------------------------------------------------------------------------------
	#
	# Events de MECANICS
	#
	# ---------------------------------------------------------------------------------------------------------------------------------------------
	#
	def on_bt_me_cancel_clicked(self,event):
		"""
		Cancela l'entrada de mecanics
		"""
		print "Cancelam nou/edicio mecanic"
		self.cancelam_fitxa("me")


	def on_bt_me_aplica_clicked(self,event):
		"""
		Acepta l'entrada de mecanics
		"""
		print "Aceptam nou/edicio mecanic"
		self.aceptam_fitxa("me")

	def on_bt_me_edita_clicked(self,event):
		"""
		Edita el mecanic
		"""
		print "Editam mecanic"
		self.editam_fitxa("me")

	def on_bt_me_nou_clicked(self,event):
		"""
		Entra un nou mecanic
		"""
		print "Nou mecanic"
		self.nova_fitxa("me")

	def on_bt_me_esborra_clicked(self,event):
		"""
		Esborra un mecanic
		"""
		print "Esborra mecanic"
		self.esborra_fitxa("me")

	def on_bt_me_primer_clicked(self,event):
		"""
		Anam al primer mecanic
		"""
		self.primera_fitxa("me")

	def on_bt_me_anterior_clicked(self,event):
		"""
		Anam al mecanic anterior
		"""
		self.anterior_fitxa("me")

	def on_bt_me_seguent_clicked(self,event):
		"""
		Anam al mecanic següent
		"""
		self.seguent_fitxa("me")

	def on_bt_me_darrer_clicked(self, event):
		"""
		Anam al darrer mecanic
		"""
		self.darrera_fitxa("me")


	def on_bt_me_cerca_clicked(self,event):
		"""
		Cercam un mecanic
		"""
		self.cerca_fitxa("me")



# 
	# ---------------------------------------------------------------------------------------------------------------------------------------------
	#
	# Events de factures
	#
	# ---------------------------------------------------------------------------------------------------------------------------------------------
	#

	def on_bt_fa_cancel_clicked(self,event):
		"""
		Cancela l'entrada de factures
		"""
		print "Cancelam nou/edicio factura"
		self.cancelam_fitxa("fa")


	def on_bt_fa_aplica_clicked(self,event):
		"""
		Acepta l'entrada de factures
		"""
		print "Aceptam nou/edicio factura"
		self.aceptam_fitxa("fa")

	def on_bt_fa_edita_clicked(self,event):
		"""
		Edita el factura
		"""
		print "Editam factura"
		self.editam_fitxa("fa")

	def on_bt_fa_nou_clicked(self,event):
		"""
		Entra un nou factura
		"""
		print "Nou factura"
		self.nova_fitxa("fa")

	def on_bt_fa_esborra_clicked(self,event):
		"""
		Esborra un factura
		"""
		print "Esborra factura"
		self.esborra_fitxa("fa")

	def on_bt_fa_primer_clicked(self,event):
		"""
		Anam al primer factura
		"""
		self.primera_fitxa("fa")

	def on_bt_fa_anterior_clicked(self,event):
		"""
		Anam al factura anterior
		"""
		self.anterior_fitxa("fa")

	def on_bt_fa_seguent_clicked(self,event):
		"""
		Anam al factura següent
		"""
		self.seguent_fitxa("fa")

	def on_bt_fa_darrer_clicked(self, event):
		"""
		Anam al darrer factura
		"""
		self.darrera_fitxa("fa")


	def on_bt_fa_cerca_clicked(self,event):
		"""
		Cercam un factura
		"""
		self.cerca_fitxa("fa")
	


	def on_bt_fa_cerca_dt_clicked(self, widget, *args):
		print "on_bt_fa_cerca_dt %s" % widget.get_name()
		data_e = self.frmcalendari.run()
		if data_e:
			an_y, mes, dia = data_e
			self.fa_data_factura.set_text( "%s/%s/%s" % (dia, mes+1, str(an_y)[2:]) )
		
	
	def on_actualitza_total(self, widget, *args):
		self.actualitza_total()
	
	def actualitza_total(self):
		""""
		Actualitza camps sub, iva, desc, total
		"""
		subtotal = 0
		for row in self.fa_liststore:
			subtotal += float( row[3] )
		self.fa_import.set_text( str(subtotal) )
		iva = subtotal * 0.16 
		descompte = 0
		try:
			descompte = float( self.fa_descompte.get_text() )
		except:
			pass
		total = subtotal + iva - descompte
		self.fa_iva.set_text( str( iva )  )
		self.fa_total.set_text( str( total ) )
		
	
	
	def on_bt_fa_inserta_ticket_clicked(self, event):
		"""
		INSERTA TICKET
		"""
		fa_ticket = FrmLlistaTicket(self.fa_client_id.get_text(), self.gjlib)
		res = fa_ticket.run()
		print res
		
		
	def on_bt_fa_inserta_linia_clicked(self, event):
		"""
		INSERTA LINIA
		"""
		descripcio =  self.linia_descripcio.get_text()
		preu = float( self.linia_preu.get_text()  )
		unitats = float(  self.linia_unitats.get_text() )
		subtotal = float(  self.linia_import.get_text() )
		linia_camp = [ descripcio, preu, unitats, subtotal ]
		print "lin: ",linia_camp
		
		self.fa_liststore.append( linia_camp )
		self.bt_fa_inserta_linia.set_sensitive( False )
		self.linia_descripcio.set_text("")
		self.linia_preu.set_text("")
		self.linia_unitats.set_text("")
		self.linia_import.set_text("")
		self.actualitza_total()
		
	def on_linia_camp(self, widget, *args):
		"""
		Comprava els camps de la linia
		"""
		preu = self.linia_preu.get_text()
		unitats = self.linia_unitats.get_text()
		if self.linia_descripcio.get_text() and preu and unitats:
			try:
				self.linia_import.set_text(  str( float( preu )*float( unitats ) ) )
				self.bt_fa_inserta_linia.set_sensitive( True )
			except:
				print "errror" 
				pass
		
		
		
	def on_bt_fa_elimina_linia_clicked(self, event):
		"""
		INSERTA ESBORRA
		"""
		treeselection = self.fa_linies_moff.get_selection()
		(model, iter) = treeselection.get_selected()
		if iter:
			self.fa_linies_moff.get_model().remove(iter)
			
		
		
		

	def on_bt_fa_client_clicked(self,event):
		"""
		Cercam el client d'una factura
		"""
		
		camps = CampsCerc()
		camps.posa_camp( "ID", int, "Codi", False )
		camps.posa_camp( "Nif", str, "DNI/NIF", True )
		camps.posa_camp( "NOM", str, "Nom", True )
		camps.posa_camp( "LLINATGES", str, "Cognoms", True )
		camps.posa_camp( "TELEFON", int, "Telèfon", True )
		camps.posa_camp( "MOBIL", int, "Telèfon Mòbil", False)
		camps.posa_camp( "DIRECCIO1", str, "Adreça", False )
		camps.posa_camp( "DIRECCIO2", str, "", False)
		camps.posa_camp( "CODIPOSTAL", int, "Codi Postal", False)
		camps.posa_camp( "POBLACIO", str, "Població", False)
		camps.posa_camp( "PAIS", str, "Pais", False )
		
		taula = "CLIENT"
		
		cerc = frmcercador.FrmCercador(camps, taula, self.gjlib )
		res = cerc.run()
		print res
		#ID de client
		self.fa_client_id.set_text( str(res[0]) )
		# Nom client
		self.fa_client_calc.set_text( "%s, %s" % (res[3], res[2]) )
		#nif
		self.fa_nif.set_text( str(res[1]) )
		#nomsocial
		self.fa_nomsocial.set_text( "%s, %s" % (res[3], res[2]) )
		#telefon
		self.fa_telefon.set_text(str(res[4]) )
		#mobil
		self.fa_mobil.set_text(str(res[5]) )
		#direccio
		self.fa_direccio1.set_text(str(res[6] ))
		self.fa_direccio2.set_text(str(res[7] ))
		#CP
		self.fa_codipostal.set_text(str(res[8] ))
		#poblacio
		self.fa_poblacio.set_text(str(res[9] ))
		#pais
		self.fa_pais.set_text(str(res[10] ))
		
		
 


# 
	# ---------------------------------------------------------------------------------------------------------------------------------------------
	#
	# Events de ARREGLOS
	#
	# ---------------------------------------------------------------------------------------------------------------------------------------------
	#

	#-- Frmgesjo.on_bt_ar_cerca_dt_entrada_clicked {
	def on_bt_ar_cerca_dt_entrada_clicked(self, widget, *args):
		print "on_bt_ar_cerca_dt_entrada_clicked called with self.%s" % widget.get_name()
		data_e = self.frmcalendari.run()
		if data_e:
			an_y, mes, dia = data_e
			self.ar_data_entrada.set_text( "%s/%s/%s" % (dia, mes+1, str(an_y)[2:]) )
		
	#-- Frmgesjo.on_bt_ar_cerca_dt_entrada_clicked }

	#-- Frmgesjo.on_bt_ar_cerca_dt_sortida_clicked {
	def on_bt_ar_cerca_dt_sortida_clicked(self, widget, *args):
		print "on_bt_ar_cerca_dt_sortida_clicked called with self.%s" % widget.get_name()
		data_e = self.frmcalendari.run()
		if data_e:
			an_y, mes, dia = data_e
			self.ar_data_sortida.set_text( "%s/%s/%s" % (dia, mes+1, str(an_y)[2:]) )
		
	#-- Frmgesjo.on_bt_ar_cerca_dt_sortida_clicked }

	#-- Frmgesjo.on_bt_ar_cerca_dt_entrega_clicked {
	def on_bt_ar_cerca_dt_entrega_clicked(self, widget, *args):
		print "on_bt_ar_cerca_dt_entrega_clicked called with self.%s" % widget.get_name()
		data_e = self.frmcalendari.run()
		if data_e:
			an_y, mes, dia = data_e
			self.ar_data_entrega.set_text( "%s/%s/%s" % (dia, mes+1, str(an_y)[2:]) )
		
	#-- Frmgesjo.on_bt_ar_cerca_dt_entrega_clicked }

	#-- Frmgesjo.on_bt_ar_cerca_dt_tornada_clicked {
	def on_bt_ar_cerca_dt_tornada_clicked(self, widget, *args):
		print "on_bt_ar_cerca_dt_tornada_clicked called with self.%s" % widget.get_name()
		data_e = self.frmcalendari.run()
		if data_e:
			an_y, mes, dia = data_e
			self.ar_data_tornada.set_text( "%s/%s/%s" % (dia, mes+1, str(an_y)[2:]) )
		
	#-- Frmgesjo.on_bt_ar_cerca_dt_tornada_clicked }



	def on_bt_ar_cancel_clicked(self,event):
		"""
		Cancela l'entrada de arreglos
		"""
		print "Cancelam nou/edicio arreglo"
		self.cancelam_fitxa("ar")


	def on_bt_ar_aplica_clicked(self,event):
		"""
		Acepta l'entrada de arreglos
		"""
		print "Aceptam nou/edicio arreglo"
		self.aceptam_fitxa("ar")

	def on_bt_ar_edita_clicked(self,event):
		"""
		Edita el arreglo
		"""
		print "Editam arreglo"
		self.editam_fitxa("ar")

	def on_bt_ar_nou_clicked(self,event):
		"""
		Entra un nou arreglo
		"""
		print "Nou arreglo"
		self.nova_fitxa("ar")

	def on_bt_ar_esborra_clicked(self,event):
		"""
		Esborra un arreglo
		"""
		print "Esborra arreglo"
		self.esborra_fitxa("ar")

	def on_bt_ar_primer_clicked(self,event):
		"""
		Anam al primer arreglo
		"""
		print "anam a primer"
		self.primera_fitxa("ar")

	def on_bt_ar_anterior_clicked(self,event):
		"""
		Anam al arreglo anterior
		"""
		self.anterior_fitxa("ar")

	def on_bt_ar_seguent_clicked(self,event):
		"""
		Anam al arreglo següent
		"""
		self.seguent_fitxa("ar")

	def on_bt_ar_darrer_clicked(self, event):
		"""
		Anam al darrer arreglo
		"""
		print "anam a darrer"
		self.darrera_fitxa("ar")


	def on_bt_ar_cerca_clicked(self,event):
		"""
		Cercam un arreglo
		"""
		self.cerca_fitxa("ar")

	def on_bt_ar_client_clicked(self,event):
		"""
		Cercam el client d'un arreglo
		"""
		
		camps = CampsCerc()
		camps.posa_camp( "ID", int, "Codi", False )
		camps.posa_camp( "Nif", str, "DNI/NIF", True )
		camps.posa_camp( "NOM", str, "Nom", True )
		camps.posa_camp( "LLINATGES", str, "Cognoms", True )
		camps.posa_camp( "TELEFON", int, "Telèfon", True )
		taula = "CLIENT"
		
		cerc = frmcercador.FrmCercador(camps, taula, self.gjlib )
		res = cerc.run()
		print res
		self.ar_client_id.set_text( str(res[0]) )
		self.ar_client_calc.set_text( "%s, %s" % (res[3], res[2]) )
		
 

	def on_bt_ar_imprimeix_clicked(self,event):
		"""
			Imprimeix l'arreglo actual
		"""
		self.imprimir_ticket()

# 
	# ---------------------------------------------------------------------------------------------------------------------------------------------
	#
	# Events de INFORMES
	#
	# ---------------------------------------------------------------------------------------------------------------------------------------------
	#


	def on_in_arreglos_tots_clicked(self,event):
		""" 
			Imprimim tots els tickets
		"""
		print "Imprimir tickets i sobres"

		posant = self.gj.fitxa_actual("ar")
		posmax = self.gj.numero_fitxes("ar")
		print posant,posmax
		inf = informes.Informes()

		self.gj.anam_registre_primer("ar")

		for x in range(posmax):

			self.imprimir_ticket()

			self.gj.anam_registre_seguent("ar")

		self.gj.anam_fitxa("ar",posant)


	def on_in_llistats_tallers_clicked(self,event):
		""" 
			Imprimim llistat de tallers
		"""
		print "Imprimir llistat de taller"

		fitxa = "me"
		print "De quin taller llistam...",fitxa
		self.dlg_taller_inicia()
		cmp_cercar = dict([ (x[2:],y)  for x,y in self.dlg_taller_run().items() if (y)])
		print cmp_cercar

		if (cmp_cercar):
			reg = self.gj.cerca(fitxa, cmp_cercar)
			print "Retorn ", reg
			if reg != None:
				pant = self.gj.registre_actual("me")
				self.gj.anam_registre("me",reg)
				r = self.gj.ret_fitxa("me")
				tid2 = r["ID"]
				nom = r["NOM"]
				tid = str(int(tid2))
				self.gj.anam_registre("me",pant)
				print tid





				self.gj.fitxaSQL["in"].executa("select ID,MARCA,MODEL, TREBALL, DATA_SORTIDA  from ARREGLO  WHERE MECANIC_ID="+tid+" order by ID")
				print self.gj.fitxaSQL["in"].num_reg,self.gj.numero_fitxes("in")

				inf = informes.Informes()

				llistat = inf.crea("llistat.pdf")

				pag = 1
				inf.cap_pagina(llistat,"Llistat de peces -- TALLER/MECANIC: "+nom,str(pag))



				linia_cap = "ID".ljust(10)+" "*4+"SORTIDA".ljust(10)+" "*4+"MARCA".ljust(10)+" "*4+"MODEL".ljust(30)+" "*5+"TREBALL".ljust(50)

				inf.cap_arreglo(llistat,linia_cap)



				self.gj.anam_registre_primer("in")

				li = 1
				print "num ....",self.gj.numero_fitxes("in")
				for x in range(self.gj.numero_fitxes("in")):
					reg = self.gj.ret_fitxa("in")
					linia = str(int(reg["ID"])).zfill(6)+" "*7+str(reg["DATA_SORTIDA"]).ljust(15)+" "*7+reg["MARCA"].ljust(15)+" "*10+reg["MODEL"].ljust(30)

					linia += " "*7+reg["TREBALL"].ljust(40)

					print "li...",linia

					inf.linia(llistat,li,linia)					
					self.gj.anam_registre_seguent("in")
					if (li ==50) or (li==100) :
						pag += 1
						inf.canvi_pagina(llistat)
						inf.cap_pagina(llistat,"Llistat de peces",str(pag))
						inf.cap_arreglo(llistat,linia_cap)


				llistat.showPage()
				llistat.save()



