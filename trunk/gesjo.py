#!/usr/bin/env python
# -*- coding: utf-8 -*-



#
# Carregam llibreries
#

import sys

try:
	import gtk
	import gtk.glade

except:
	print "Necessites tenir instalat el pyGTK o GTK2, ",
	print "o posar correctament el PYTHONPATH. També són",
	print "necessàries les llibreries libglade..."
	sys.exit(1)



#
# Splash
#
def actbarra(wid, val):
	wid.set_fraction(val)
	while gtk.events_pending():
		gtk.main_iteration()

try:
	splash = gtk.Window(gtk.WINDOW_TOPLEVEL)
	splash.set_decorated(False)
	splash.set_border_width(10)
	splash.set_position(gtk.WIN_POS_CENTER)

	caixa = gtk.VBox(False,0)
	splash.add(caixa)


	caixa2 = gtk.HBox(False,0)
	imatge = gtk.Image()
	imatge.set_from_file("./recursos/pixmaps/rellotge.xpm")
	caixa2.pack_start(imatge, True, True, 3)
	imatge.show()

	linia = gtk.Label("")
	linia.set_use_markup(True)
	linia.set_markup("<i><b>Gesjo</b> - Gestió Joeiera</i>\n\nVersió 0.1.1 BETA\n\nper Josep Torrens, (C) GPL 2004.\n\n")
	caixa2.pack_start(linia, True, True, 3)
	linia.show()

	caixa2.show()
	caixa.pack_start(caixa2,True, True,3)

	pro = gtk.ProgressBar()
	pro.set_text("Iniciant...")
	pro.set_fraction(0.10)

	caixa.pack_start(pro,True, True,3)
	pro.show()

	caixa.show()
	splash.show()
	while gtk.events_pending():
		gtk.main_iteration()
except:
		pass



#
# Carregam llibreries
#
import reportlab as rpt
actbarra(pro,0.20)
import os
actbarra(pro,0.25)
import basedades
actbarra(pro,0.30)
import types
actbarra(pro,0.35)
import gjlib
actbarra(pro,0.40)
import ww
actbarra(pro,0.50)
import wdialeg
actbarra(pro,0.60)

class Gesjo:
	""" Classe Gesjo """
	def __init__( self, basededades, usuari, clau ):



		self.bd = basedades.BaseDades()

		# Conectam
		res = self.bd.connexio( basededades, usuari, clau , "5433")
		if (not res):
			dlg = wdialeg.WidDlg("<big><b>Àvis!!!</b>, no s'ha pogut conectar a\n la base de dades.</big>",False, None)
			rc = dlg.run()

			sys.exit(1)

		self.gj = gjlib.GJLib(self.bd)
		self.comp = ww.WidApp(self.gj)
##		self.comp.new()
		
		self.gj.anam_fitxa("cl",1)
		self.comp.mostra_fitxa("cl")
		#self.gj.anam_fitxa("ar",1)
		self.comp.run()


#
# Cream
#
print sys.getdefaultencoding()
actbarra(pro,0.95)
splash.destroy()
gesjo_app = Gesjo( "gjdb", "josep", "coder69" )



gtk.main()

