#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import gtk
import gobject

class prova:
	def delete_event(self, widget, event, data=None):
		gtk.main_quit()
		return gtk.FALSE
	
	def __init__(self):
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.set_title("AA")
		self.window.connect("delete_event",self.delete_event)
		
	
	def crea_model(self, tcols):
	
		self.llista = gtk.ListStore(tcols)
	
	def fica_fila(self, dades):
		fila = self.llista.append()
		for i in range(len(dades)-1):
			print i,len(dades)
			self.llista.set(fila, i,dades[i])
		
		
	def run(self,cols):
		self.grid = gtk.TreeView(self.llista)
		
		for i,j in zip(cols,range(len(cols))):
			self.tvcol =gtk.TreeViewColumn(i)
			self.grid.append_column(self.tvcol)
			
			self.cell = gtk.CellRendererText()
			
			self.tvcol.pack_start(self.cell,True)
			
			self.tvcol.add_attribute(self.cell,'text',j)
			
			self.grid.set_search_column(j)
			
			self.tvcol.set_sort_column_id(j)
			
			self.grid.set_reorderable(True)
			
	
		self.window.add(self.grid)
		self.window.show_all()
		
	def main(self):
		gtk.main()
		
if __name__ == "__main__":
		tvllista = prova()
		tvllista.crea_model(str)
		tvllista.fica_fila(["PROVAssdsd"])
		tvllista.run("aque si")
		tvllista.main()
		
