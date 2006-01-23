#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Classe del GUI
# 

import gtk
import gtk.glade
import types
import new
##import wdialeg
import gobject
import informes 
import datetime as data
import sys

from SimpleGladeApp import AppBase
from SimpleGladeApp import bindtextdomain
##from pre_dbl import PrefixDBL


app_name = "Gesjo"
app_version = "0.2.1"

glade_dir = "./glade"
locale_dir = ""

bindtextdomain(app_name, locale_dir)

class WidApp(AppBase):
	def __init__( self, fitxer, gjlib, path="Gesjo", root="frmgesjo", domain=app_name, **kwargs ):
		path = os.path.join(glade_dir, path)
		
		AppBase.__init__(self, path, root, domain, **kwargs)
		
		self.gj = gjlib
		self.fitxer = fitxer
		self.widgets = gtk.glade.XML(fitxer)
		self.widgets.signal_autoconnect(self) 

		self.wid = self.widgets.get_widget

		#
		# Senyals pels botons de tancar finestres
		#
		self.wid('frmmarca').connect("delete_event",self.on_ma_delete_event)
		self.wid('frmtaller').connect("delete_event",self.on_ta_delete_event)
		self.wid('frmmecanic').connect("delete_event",self.on_ta_delete_event)
		self.wid('frmbrowse').connect("delete_event",self.on_sel_delete_event)
		self.wid('frmgesjo').connect("delete_event",gtk.main_quit)

		self.camps_cercar = []
		self.valors_cercar = []

		self.camps_editats = {}
		self.camps_editats["cl"] = []
		self.camps_editats["ma"] = []
		self.camps_editats["ta"] = []
		self.camps_editats["me"] = []
		self.camps_editats["ar"] = []

		self.edita = {}

		# eliminam les petanyes de la dreta
		self.wid("pestanya").set_show_tabs( False )


	def mostra_fitxa(self,fitxa):
			""" fica les dades del registre actual
			a la fitxa donada (del gui) """
			res = {}
			res = self.gj.ret_fitxa(fitxa)
			if res:
				print "mostram fitxa %s...." % fitxa
				print "...",res
				print ".........",res.keys()


				for cmp in map(str.lower,res.keys()):
					w = "%s_%s" % (fitxa, cmp)
					print "camp...",w

					#~ Miram si hi ha claus foranees
					#~ .
					if cmp.endswith("_id"):
						print "Hem trobat la clau foranea...",cmp
						taularef,codi = cmp.split("_")
						fitxaref = taularef[:2]
						cercam = {}



						# Si la clau no es nula, cercam el valor associat
						if res[cmp]:
							cercam["id"] = int(res[cmp])
							regcerc = self.gj.cerca(fitxaref,cercam)
							self.gj.anam_fitxa(fitxaref,regcerc)
							reg = self.gj.ret_fitxa(fitxaref)
							print "%s-%s" % (fitxa, taularef)
							print "reg...",reg["NOM"]
							self.wid("%s-%s" % (fitxa, taularef)).set_text(reg['NOM'])



					if (type(self.wid(w)) is gtk.TextView):
						if res[cmp]==None:
							res[cmp] = ""	
						self.wid(w).get_buffer().set_text(res[cmp].replace("~","'"))
					else:
						try:
							print "miram si es dats",cmp
							if cmp.startswith("data_"):
								any,mes,dia = str(res[cmp]).split("-")
								v = "%s/%s/%s" % (dia,mes,any)
							else:
								print "miram si es grs-kts",cmp
								if cmp.endswith("_fl"):
									v = unicode(float(res[cmp])).zfill(5)
								else:
									print "numero",cmp
									v = unicode(int(res[cmp])).zfill(5)
									#~ v = str(int(res[cmp])).decode('utf-8').zfill(5)


						except:
							print "miram perque error",cmp
							if res[cmp]==None:
								v = ""
							else:
								v = unicode(str(res[cmp]).replace("~","'"))
							#~ v = str(res[cmp]).decode('utf-8')

						self.wid(w).set_text(v)





	def on_btsurt_clicked(self,event):
		print "Sortint..."
		gtk.main_quit()
		sys.exit(0)


	def on_btarreglos_clicked(self,event):
		print "Anam a arreglos"
		self.wid('pestanya').set_current_page(1)
		self.mostra_fitxa("ar")

	def on_btclients_clicked(self,event):
		print "Anam a clients"
		self.wid('pestanya').set_current_page(0)		
		self.mostra_fitxa("cl")

	def on_btinformes_clicked(self,event):
		print "Anam a informes"
		self.wid('pestanya').set_current_page(3)		


#~ ----------------------------------------------------------------------------------------------------------------------------------		
 #~ Events pels menus
 #~ ----------------------------------------------------------------------------------------------------------------------------------

	def on_mnsurt_activate(self,event):
		print "Sortint..."
		gtk.main_quit()

	def  on_mnmarques_activate_item(self,event):
		print "Manteniment de Marques"
		self.mostra_fitxa("ma")
		self.wid('frmmarca').show()


	def on_mntallers_activate_item(self,event):
		print "Manteniment de Tallers"
		self.mostra_fitxa("ta")
		self.wid('frmtaller').show()


	def on_mnmecanics_activate_item (self,event):
		print "Manteniment de Mecanics"
		self.mostra_fitxa("me")
		self.wid('frmmecanic').show()

 #~ ----------------------------------------------------------------------------------------------------------------------------------
 #~ Events de tancar les finestres
 #~ -----------------------------------------------------------------------------------------------------------------------------------


	#
	# Tallers
	#
	#
	def on_ta_delete_event(self, *args):
		self.wid('frmtaller').hide()
		return gtk.TRUE


	def on_bt_ta_tanca_clicked(self,event):
		self.wid('frmtaller').hide()


	#
	# Mecanics
	#
	#
	def on_me_delete_event(self, *args):
		self.wid('frmmecanic').hide()
		return gtk.TRUE


	def on_bt_me_tanca_clicked(self,event):
		self.wid('frmmecanic').hide()






	def on_bt_me_cerca_taller_clicked(self,event):
		#~ self.wid('frmbrowse').show()
		#~ brw = self.wid('brw')


		#~ model = self.create_model([1,"PROVA"])

		#~ treeview = gtk.TreeView(model)
		#~ treeview.set_rules_hint(TRUE)
		#~ treeview.set_search_column(COLUMN_DESCRIPTION)

		#~ sw.add(treeview)


		#~ treeview.append_column(column)
		#~ brw = treeview


		#~ brw.show_all()
		pass


	#
	# Marques
	#
	#
	def on_ma_delete_event(self, *args):
		self.wid('frmmarca').hide()
		return gtk.TRUE


	def on_bt_ma_tanca_clicked(self,event):
		self.wid('frmmarca').hide()

	#
	# Seleccionador
	#
	#
	def on_sel_delete_event(self, *args):
		self.wid('frmbrowse').hide()
		return gtk.TRUE

	def on_bt_sel_cancel_clicked(self,event):
		self.wid('frmbrowse').hide()

	def on_bt_sel_si_clicked(self,event):
		self.wid('frmbrowse').hide()




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





	def editam_fitxa(self,fitxa):
		"""
		L'usuari edita una fitxa
		"""
		print "Editam ",fitxa

		self.edita[fitxa] = True

		self.wid('bt_'+fitxa+'_aplica').show()
		self.wid('bt_'+fitxa+'_cancel').show()

		for x in self.widgets.get_widget_prefix(fitxa+"_"):

			if type(x) is gtk.TextView:
				y =x.get_buffer()
				inici_iter, final_iter = y.get_bounds()
				self.camps_editats[fitxa].append(y.get_text(inici_iter,final_iter))
			else:
				self.camps_editats[fitxa].append(x.get_text())
				print  x.get_text()


	def nova_fitxa(self,fitxa):
		"""
		L'usuari fa una nova fitxa
		"""
		print "Nova fitxa"

		self.edita[fitxa] = False

		for x in self.widgets.get_widget_prefix(fitxa+"_"):
##			print x.get_name()

			if type(x) is gtk.TextView:
				y =x.get_buffer()
				inici_iter, final_iter = y.get_bounds()
				self.camps_editats[fitxa].append(y.get_text(inici_iter,final_iter))
				y.set_text("")
			else:
				self.camps_editats[fitxa].append(x.get_text())
				print  x.get_text()
				x.set_text("")
			if x.get_name().startswith(fitxa+"_data_entra"):
				x.set_text(data.date.today().strftime("%d/%m/%y"))

		self.wid('bt_'+fitxa+'_aplica').show()
		self.wid('bt_'+fitxa+'_cancel').show()

		if ( fitxa == "cl" ):
			self.wid(fitxa+"_nom").grab_focus()

	def cancelam_fitxa(self,fitxa):
		"""
		L'usuari cancela l'entrada o
		modificacio de la fitxa
		"""
		print "Cancelam nou/edicio ",fitxa
		self.wid('bt_'+fitxa+'_aplica').hide()
		self.wid('bt_'+fitxa+'_cancel').hide()

		self.edita[fitxa] = False

		for x,y in zip(self.widgets.get_widget_prefix(fitxa+"_"),self.camps_editats[fitxa]):
			if type(x) is gtk.TextView:
				x.get_buffer().set_text(y)
			else:
				x.set_text(y)
		self.camps_editats[fitxa] = []


	def aceptam_fitxa(self,fitxa):
		"""
		L'usuari acepta/valida
		l'entrada o modificacio de
		la fitxa
		"""
		print "Aceptam nou/edicio ",fitxa

		fit = {}

		for x in self.widgets.get_widget_prefix(fitxa+"_"):
			if type(x) is gtk.TextView:
				y =x.get_buffer()
				inici_iter, final_iter = y.get_bounds()
				fit[x.get_name()]=y.get_text(inici_iter,final_iter)
			else:
				fit[x.get_name()]=x.get_text()

		print "fitxa..."
		print fit
#		try:
		if (self.edita[fitxa]):
			self.gj.modifica_fitxa(fitxa,fit)
		else:
			self.gj.inserta_fitxa(fitxa,fit)

		self.camps_editats[fitxa] = []
		self.wid('bt_'+fitxa+'_aplica').hide()
		self.wid('bt_'+fitxa+'_cancel').hide()

		self.edita[fitxa] = False

	#	except:

#		dlg = wdialeg.WidDlg("<big><b>Error de dades!</b>\nComprova que les dades són correctes.</big>\n\nEn particular comprova que no hi ha dades\n no numériques en els camps numérics.",False, None)
#			rc = dlg.run()


	def esborra_fitxa(self,fitxa):
		""" 
		L'usuari esborra una fitxa
		"""
		print "Esborra fitxa"

		dlg = wdialeg.WidDlg("<big>Segur que vols <b>esborrar</b>\n aquesta fitxa ? </big>",True, None)
		rc = dlg.run()
		print "Tria ",rc
		if (rc): 
			self.gj.borra_fitxa(fitxa,self.wid(fitxa+"_id").get_text())
			print "Fet"
			self.darrera_fitxa(fitxa)

	def primera_fitxa(self,fitxa):
		"""
		Anar a la primera fitxa
		"""
		print "Anam a la primera ",fitxa
		self.gj.anam_registre_primer(fitxa)
		self.mostra_fitxa(fitxa)
		print "som a %s..." % fitxa,self.gj.registre_actual(fitxa)

	def anterior_fitxa(self,fitxa):
		"""
		Anam a la fitxa anterior
		"""
		print "Anam a l'anterior ",fitxa
		self.gj.anam_registre_anterior(fitxa)
		self.mostra_fitxa(fitxa)
		print "som a %s..." % fitxa,self.gj.registre_actual(fitxa)

	def seguent_fitxa(self,fitxa):
		"""
		Anam a la fitxa següent
		"""
		print "Anam a la següent ", fitxa
		self.gj.anam_registre_seguent(fitxa)
		self.mostra_fitxa(fitxa)
		print "som a %s..." % fitxa,self.gj.registre_actual(fitxa)


	def darrera_fitxa(self, fitxa):
		"""
		Anam a la darrera fitxa
		"""
		print "Anam a la darrera ", fitxa
		self.gj.anam_registre_darrer(fitxa)
		self.mostra_fitxa(fitxa)
		print "som a %s..." % fitxa,self.gj.registre_actual(fitxa)

	def cerca_fitxa(self,fitxa):
		"""
		Cercam una fitxa
		"""
		print "Cercam fitxa de",fitxa
		if (fitxa == "cl"):
			self.dlg_cerca_inicia()
			cmp_cercar = self.dlg_cerca_run()
		else:
			self.dlg_cerca_ar_inicia()
			cmp_cercar = self.dlg_cerca_ar_run()
##		cmp_cercar = dict([ (x[2:],y)  for x,y in self.dlg_cerca_run().items() if (y)])
##		cmp_cercar = dict( ([x[2:]]:y  for x,y in self.dlg_cerca_run().camps_cercar if (y)])
##		cmp_cercar = dict([ (x[2:],self.dlg_cerca_run.camps_cercar[x]) for x in self.dlg_cerca_run.camps_cercar.keys() if (self.dlg_cerca_run.camps_cercar[x])])
		if (cmp_cercar):
			reg = self.gj.cerca(fitxa, cmp_cercar)
			print "Retorn ", reg
			if reg != None:
				self.mostra_fitxa(fitxa)






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
		self.cerca_fitxa("cl")

	# 
	# ---------------------------------------------------------------------------------------------------------------------------------------------
	#
	# Events de MARQUES
	#
	# ---------------------------------------------------------------------------------------------------------------------------------------------
	#
	def on_bt_ma_cancel_clicked(self,event):
		"""
		Cancela l'entrada de marcas
		"""
		print "Cancelam nou/edicio marca"
		self.cancelam_fitxa("ma")


	def on_bt_ma_aplica_clicked(self,event):
		"""
		Acepta l'entrada de marcas
		"""
		print "Aceptam nou/edicio marca"
		self.aceptam_fitxa("ma")

	def on_bt_ma_edita_clicked(self,event):
		"""
		Edita el marca
		"""
		print "Editam marca"
		self.editam_fitxa("ma")

	def on_bt_ma_nou_clicked(self,event):
		"""
		Entra un nou marca
		"""
		print "Nou marca"
		self.nova_fitxa("ma")

	def on_bt_ma_esborra_clicked(self,event):
		"""
		Esborra un marca
		"""
		print "Esborra marca"
		self.esborra_fitxa("ma")

	def on_bt_ma_primer_clicked(self,event):
		"""
		Anam al primer marca
		"""
		self.primera_fitxa("ma")

	def on_bt_ma_anterior_clicked(self,event):
		"""
		Anam al marca anterior
		"""
		self.anterior_fitxa("ma")

	def on_bt_ma_seguent_clicked(self,event):
		"""
		Anam al marca següent
		"""
		self.seguent_fitxa("ma")

	def on_bt_ma_darrer_clicked(self, event):
		"""
		Anam al darrer marca
		"""
		self.darrera_fitxa("ma")


	def on_bt_ma_cerca_clicked(self,event):
		"""
		Cercam un marca
		"""
		self.cerca_fitxa("ma")


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
	# Events de ARREGLOS
	#
	# ---------------------------------------------------------------------------------------------------------------------------------------------
	#

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





#~ ----------------------------------------------------------------------------------------------------------------------------------	
#~ Els dialegs
#~ ----------------------------------------------------------------------------------------------------------------------------------

	def dlg_cerca_inicia(self):
		self.wid('dlg_cerca').set_transient_for(self.wid('frmgesjo'))
		self.wid('CERCB').connect("clicked", self.CECB)
		self.wid('CANCB').connect("clicked", self.CACB)

		self.wid('dlg_cerca').set_modal(gtk.TRUE)

	def dlg_cerca_run(self):
		"""Run the modal dialog.  Return whatever the user entered."""
		# This is a little weird.  Basically just run a nested
		# mainloop, and exit the mainloop by mainquit()-ing
		# out of the nested loop.  (See self.OKCB)

		for c in self.widgets.get_widget_prefix("v_") :
				c.set_text("")

		self.wid('dlg_cerca').show()
		gtk.main()

		return self.camps_cercar

	def CECB(self, *args):
		  """Callback invoked when the Cercar button is clicked."""
		  # In theory, this would be a good place to validate user input
		  # before committing changes.  In practice...

##		  self.camps_cercar = [ c.name for c in self.widgets.get_widget_prefix("c_") ]
##		  self.camps_valors = [ self.wid("v_"+x).get_text() for x in [ y[2:] for y in self.camps_cercar] ]
		  x = [ (c.name)[2:] for c in self.widgets.get_widget_prefix("c_")]
		  y = [ self.widgets.get_widget("v_"+v).get_text() for v in x ]

		  self.camps_cercar = dict( [ (a,b) for a,b in zip(x,y) if b!=""] )
##		  self.camps_cercar = dict(zip(x,y))
##		  self.cmp_cercar = dict( c.name[2:],self.widgets.get_widget_prefix("v_").get_text()) for x in self.widgets.get_widget_prefix("c_"))
		  self.wid('dlg_cerca').hide()
		  gtk.main_quit()


	def CACB(self, *args):
		"""Callback invoked when the OK button is clicked."""
		# In theory, this would be a good place to validate user input
		# before committing changes.  In practice...
##		self.camps_cercar = []
		self.camps_cercar = {}
		self.camps_valors = []
		self.wid('dlg_cerca').hide()
		gtk.main_quit()


	def dlg_cerca_ar_inicia(self):
		self.wid('dlg_cerca_ar').set_transient_for(self.wid('frmgesjo'))
		self.wid('TACB').connect("clicked", self.TACB)
		self.wid('CATCB').connect("clicked", self.CATCB)

		self.wid('dlg_cerca_ar').set_modal(gtk.TRUE)

	def dlg_cerca_ar_run(self):
		"""Run the modal dialog.  Return whatever the user entered."""
		# This is a little weird.  Basically just run a nested
		# mainloop, and exit the mainloop by mainquit()-ing
		# out of the nested loop.  (See self.OKCB)

		for c in self.widgets.get_widget_prefix("va_") :
				c.set_text("")

		self.wid('dlg_cerca_ar').show()
		gtk.main()

		return self.camps_cercar

	def TACB(self, *args):
		"""Callback invoked when the Cercar button is clicked."""
		# In theory, this would be a good place to validate user input
		# before committing changes.  In practice...
##		self.camps_cercar = zip([c.name for c in self.widgets.get_widget_prefix("c_")],[v.get_text() for v in self.widgets.get_widget_prefix("v_")] )
		x = [ (c.name)[3:] for c in self.widgets.get_widget_prefix("ca_")]
		y = [ self.widgets.get_widget("va_"+v).get_text() for v in x ]
		self.camps_cercar = dict( [ (a,b) for a,b in zip(x,y) if b!=""] )

##		  self.camps_cercar = dict( [ (a,b) for a,b in zip(x,y) if b!=""] )

##		self.camps_cercar = [ c.name for c in self.widgets.get_widget_prefix("c_") ]
##		self.camps_valors = [ self.wid("v_"+x).get_text() for x in [ y[2:] for y in self.camps_cercar] ]
		self.wid("dlg_cerca_ar").hide()


		gtk.main_quit()


	def CATCB(self, *args):
		"""Callback invoked when the OK button is clicked."""
		# In theory, this would be a good place to validate user input
		# before committing changes.  In practice...
		self.camps_cercar = []
		self.camps_valors = []
		self.wid('dlg_cerca_ar').hide()
		gtk.main_quit()


