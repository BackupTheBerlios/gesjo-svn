#
# Classe del GUI
# 

import gtk
import  gtk.glade
import types
import new
import wdialeg

	
class WidApp:
	def __init__(self, fitxer, gjlib):
		self.gj = gjlib
		self.fitxer = fitxer
		self.widgets = gtk.glade.XML(fitxer)
		self.widgets.signal_autoconnect(self) 

		self.wid = self.widgets.get_widget
		
		#
		# Senyals pels botons de tancar finestres
		#
		self.wid('frmmarca').connect("delete_event",self.on_ma_delete_event)
		self.wid('frmgesjo').connect("delete_event",gtk.main_quit)

		self.camps_cercar = []
		self.valors_cercar = []

		self.camps_editats = []


	def mostra_fitxa(self,fitxa):
			""" fica les dades del registre actual
			a la fitxa donada (del gui) """
			res = self.gj.ret_fitxa(fitxa)
			print "mostram fitxa %s...." % fitxa
			
			for cmp in map(str.lower,res.keys()):
				w = "%s_%s" % (fitxa, cmp)
				if (type(self.wid(w)) is gtk.TextView):
					self.wid(w).get_buffer().set_text(str(res[cmp]))
				else:
					if (cmp=="codipostal"):
						self.wid(w).set_text(str(res[cmp]).zfill(5))
					else:
						self.wid(w).set_text(str(res[cmp]))
	



	def on_btsurt_clicked(self,event):
		print "Sortint..."
		gtk.main_quit()

	def on_btarreglos_clicked(self,event):
		print "Anam a arreglos"
		self.wid('pestanya').set_current_page(1)
		
	def on_btclients_clicked(self,event):
		print "Anam a clients"
		self.wid('pestanya').set_current_page(0)		
	
	#
	# Events pels menus
	def on_mnsurt_activate(self,event):
		print "Sortint..."
		gtk.main_quit()
	
	def  on_mnmarques_activate_item(self,event):
		print "Manteniment de Marques"
		self.mostra_fitxa("ma")
		self.wid('frmmarca').show()
		
	
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
	# Events pel dialeg "confirmar eliminar"
	def on_bt_dl_esborra_cancel_clicked(self,event):
		print "L'usuari ha cancelat l'esborrar"
		self.wid('frm_dl_esborra').hide()

		
	def on_bt_dl_dacord_clicked(self,event):
		print "L'usuari ha confirmat que vol esborrar"
		print " la fitxa ",fitxa
		self.wid('frm_dl_esborra').hide()
		#self.gj.borra_fitxa(fitxa)

	#
	# Events per la pagina de clients
	def on_bt_cl_cancel_clicked(self,event):
		print "Cancelam nou/edicio client"
		self.wid('bt_cl_aplica').hide()
		self.wid('bt_cl_cancel').hide()
		
		for x,y in zip(self.widgets.get_widget_prefix("cl_"),self.camps_editats):
			if type(x) is gtk.TextView:
				x.get_buffer().set_text(y)
			else:
				x.set_text(y)
		self.camps_editats = []
		
		
	def on_bt_cl_aplica_clicked(self,event):
		print "Aceptam nou/edicio client"
		
		fit = []
		
		fit.append(self.wid("cl_nom").get_text())
		fit.append(self.wid("cl_llinatges").get_text())
		fit.append(self.wid("cl_direccio1").get_text())
		fit.append(self.wid("cl_direccio2").get_text())
		fit.append(self.wid("cl_poblacio").get_text())
		fit.append(self.wid("cl_codipostal").get_text())
		fit.append(self.wid("cl_telefon").get_text())
		fit.append(self.wid("cl_mobil").get_text())
		fit.append(self.wid("cl_email").get_text())
		fit.append("nota ") # posar notes
		fit.append(self.wid("cl_pais").get_text())
		try:
			self.gj.inserta_fitxa("cl",fit)
			self.on_bt_cl_darrer_clicked(event)
			self.camps_editats = []
			self.wid('bt_cl_aplica').hide()
			self.wid('bt_cl_cancel').hide()
		
		except ValueError:
			
			dlg = wdialeg.WidDlg("<big><b>Error de dades!</b>\nComprova que les dades són correctes.</big>\n\nEn particular comprova que no hi ha dades\n no numériques en els camps numérics.",False, None)
			rc = dlg.run()

		
	
	def on_bt_cl_edita_clicked(self,event):
		print "Editam client"
		self.wid('bt_cl_aplica').show()
		self.wid('bt_cl_cancel').show()
		
		for x in self.widgets.get_widget_prefix("cl_"):
			
			if type(x) is gtk.TextView:
				y =x.get_buffer()
				inici_iter, final_iter = y.get_bounds()
				self.camps_editats.append(y.get_text(inici_iter,final_iter))
			else:
				self.camps_editats.append(x.get_text())
	
	
	def on_bt_cl_nou_clicked(self,event):
		print "Nou client"
		
		for x in self.widgets.get_widget_prefix("cl_"):
			
			if type(x) is gtk.TextView:
				y =x.get_buffer()
				inici_iter, final_iter = y.get_bounds()
				self.camps_editats.append(y.get_text(inici_iter,final_iter))
			else:
				self.camps_editats.append(x.get_text())
	
		
		self.wid("cl_nom").set_text("")
		self.wid("cl_llinatges").set_text("")
		self.wid("cl_direccio1").set_text("")
		self.wid("cl_direccio2").set_text("")
		self.wid("cl_codipostal").set_text("")
		self.wid("cl_telefon").set_text("")
		self.wid("cl_email").set_text("")
		self.wid("cl_notes").get_buffer().set_text("")
		self.wid("cl_pais").set_text("")
		
		self.wid('bt_cl_aplica').show()
		self.wid('bt_cl_cancel').show()
		
		
	def on_bt_cl_esborra_clicked(self,event):
		print "Esborra client"
		
		dlg = wdialeg.WidDlg("<big>Segur que vols <b>esborrar</b>\n aquest client? </big>",True, None)
		rc = dlg.run()
		print "Tria ",rc
		if (rc): 
			self.gj.borra_fitxa("cl",self.wid("cl_id").get_text())
			print "Fet"
			self.on_bt_cl_darrer_clicked(event)
		
		
	def on_bt_cl_primer_clicked(self,event):
		print "primer client"
		print "som a CL...",self.gj.registre_actual("cl")
		self.gj.anam_registre_primer("cl")
		self.mostra_fitxa("cl")
		print "som a CL...",self.gj.registre_actual("cl")
		
	def on_bt_cl_anterior_clicked(self,event):
		print "anterior client"
		
		print "som a CL...",self.gj.registre_actual("cl")
		self.gj.anam_registre_anterior("cl")
		self.mostra_fitxa("cl")
		print "som a CL...",self.gj.registre_actual("cl")
		
		print "Compara...",self.gj.registre_actual("cl") -1, " amb 0"
		print self.gj.registre_actual("cl") -1 >= 0
		
	
	def on_bt_cl_seguent_clicked(self,event):
		print "seguent client"
	
		print "som a CL...",self.gj.registre_actual("cl")
		self.gj.anam_registre_seguent("cl")
		self.mostra_fitxa("cl")
		print "som a CL...",self.gj.registre_actual("cl")
		
		
	def on_bt_cl_darrer_clicked(self, event):
		print "darrer client"
		
		print "som a CL...",self.gj.registre_actual("cl")
		self.gj.anam_registre_darrer("cl")
		self.mostra_fitxa("cl")
		print "som a CL...",self.gj.registre_actual("cl")
		
	def on_bt_cl_cerca_clicked(self,event):
		print "Cercam client"
		self.dlg_cerca_inicia()
		cmp_cercar = dict([ (x[2:],y)  for x,y in self.dlg_cerca_run().items() if (y)])
		
		if (cmp_cercar):
			reg = self.gj.cerca("cl",cmp_cercar)
			print "Retorn ", reg
			if reg != None:
				self.mostra_fitxa("cl")

	#
	# Events per la pagina d'arreglos
	def on_bt_ar_edita_clicked(self,event):
		print "Editam arreglo"
		self.wid('bt_ar_aplica').show()
		self.wid('bt_ar_cancel').show()
		
	def on_bt_ar_cancel_clicked(self,event):
		print "Cancelam edicio arreglo"
		self.wid('bt_ar_aplica').hide()
		self.wid('bt_ar_cancel').hide()
		
	def on_bt_ar_nou_clicked(self,event):
		print "Nou arreglo"
		
	def on_bt_ar_esborra_clicked(self,event):
		print "Esborra arreglo"
		self.wid('dl_esborra').set_markup("<b>Segur que vol esborrar</b>\n <u>aquest arreglo</u>?")
		self.wid('frm_dl_esborra').show()
		
	

	#
	# Pels dialegs
	#
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
		
		if (self.camps_cercar != []):
				return dict(zip(self.camps_cercar, self.camps_valors))
		else:
			return {}
	
	def CECB(self, *args):
		"""Callback invoked when the Cercar button is clicked."""
		# In theory, this would be a good place to validate user input
		# before committing changes.  In practice...
					
		self.camps_cercar = [ c.name for c in self.widgets.get_widget_prefix("c_") ]
		self.camps_valors = [ self.wid("v_"+x).get_text() for x in [ y[2:] for y in self.camps_cercar] ]
		
		self.wid('dlg_cerca').hide()
		gtk.main_quit()
		
		
	def CACB(self, *args):
		"""Callback invoked when the OK button is clicked."""
		# In theory, this would be a good place to validate user input
		# before committing changes.  In practice...
		self.camps_cercar = []
		self.camps_valors = []
		self.wid('dlg_cerca').hide()
		gtk.main_quit()
		

	#
	# ***** Recerques*****
	#
	