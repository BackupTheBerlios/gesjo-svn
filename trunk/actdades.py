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

def acttitol(wid, tit):
    wid.set_text(tit)


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
	linia.set_markup("<i><b>Gesjo</b> - Gestió Joeiera</i>\nMigracio de dades.\n\n")
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

import csv



acttitol(pro,"Carregant clients")
actbarra(pro,0.20)

#
# CLIENTS
#
#
sql_clients = []
f_client= "dades/client.csv"
dades_clients = file(f_client).readlines()

#Llegim els camps
camps_clients = dades_clients[0].replace("\r\n","").split(",")
camps_clients.remove("ID")
#Eliminam la linia de camps
dades_clients.pop(0)
#Convertim camps a un string
strcamp_clients = ",".join(camps_clients)

acttitol(pro,"Llegint clients")
actbarra(pro,0.30)

#tractam linies de clients
for i in csv.reader(dades_clients):
	d = list(i)
	d.pop(0)
	d = [ ("\"%s\"" % x) for x in d ]
	strval_clients = ",".join(d)
	sql_clients.append( "INSERT INTO CLIENTS (%s) VALUES(%s)" % (strcamp_clients, strval_clients) )
	
print sql_clients


acttitol(pro,"Carregant arreglos")
actbarra(pro,0.60)


#
# ARREGLOS
#
#
sql_arreglos = []
f_arreglos= "dades/arreglo.csv"
dades_arreglos = file(f_arreglos).readlines()

camps_arreglos = dades_arreglos[0].replace("\r\n","").split(",")
camps_arreglos.remove("ID")

dades_arreglos.pop(0)

strcamp_arreglos = ",".join(camps_arreglos)

acttitol(pro,"Llegint arreglos")
actbarra(pro,0.70)



for i in csv.reader(dades_arreglos):
	d = list(i)
	d.pop(0)
	d = [ ("\"%s\"" % x) for x in d ]
	strval_arreglos = ",".join(d)
	sql_arreglos.append( "INSERT INTO CLIENTS (%s) VALUES(%s)" % (strcamp_arreglos, strval_arreglos) )
	
print sql_arreglos

acttitol(pro,"Insertant..")
actbarra(pro,0.90)

	
	




