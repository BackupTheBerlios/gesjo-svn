#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Classes de dialegs
#
import gtk

class WidDlg:
	"""This is just a sample modal dialog."""
	
	def __init__(self, msg,pregunta=False,master=None):
		"""Initialize a new instance.
		`master' (optional) is the gtk.Window by which this dialog is
		launched.  `master' is needed only so we can tell the window
		manager that the dialog is a transient window for some other
		window, so it should have transient window decorations."""
	
		self.master = master
	
		self.window = gtk.Dialog()
		if self.master:
			self.window.set_transient_for(self.master)
	
		# Estat, valor que retornam
		self.estat = False
		
		# Dialogs come with containers built in: vbox for the custom
		# controls, and action_area for the dialog buttons.
		hbox = gtk.HBox()
		self.window.vbox.pack_start(hbox)
		hbox.show()
	
		
		imatge = gtk.Image()
		imatge.use_stock = True
		imatge.set_from_stock(gtk.STOCK_DIALOG_WARNING,gtk.ICON_SIZE_DIALOG)
		hbox.pack_start(imatge)
		imatge.show()
		
		linia = gtk.Label("")
		linia.set_use_markup(True)
		linia.set_markup(msg)
		hbox.pack_start(linia)
		linia.show()
	
		
		self.okBtn = gtk.Button("OK")
		self.okBtn.connect("clicked", self.OKCB)
		self.window.action_area.pack_start(self.okBtn, expand=False)
		self.okBtn.show()
	
		if (pregunta == True):
			self.canBtn = gtk.Button(" CANCELA ")
			self.canBtn.connect("clicked", self.CANCB)
			self.window.action_area.pack_start(self.canBtn, expand=False)
			self.canBtn.show()
		
		
		# Tell gtk.+ this is a modal dialog.  Pop it up wherever
		# the mouse is at the time of popup.
		self.window.set_modal(True)
		self.window.set_position(gtk.WIN_POS_CENTER_ALWAYS)
		

	def run(self):
		"""Run the modal dialog.  Return whatever the user entered."""
		# This is a little weird.  Basically just run a nested
		# mainloop, and exit the mainloop by mainquit()-ing
		# out of the nested loop.  (See self.OKCB)
		self.window.show()
		gtk.main()
		return self.estat
	
	def OKCB(self, *args):
		"""Callback invoked when the OK button is clicked."""
		# In theory, this would be a good place to validate user input
		# before committing changes.  In practice...
		self.window.hide()
		gtk.main_quit()
		self.estat= True
		
	def CANCB(self, *args):
		"""Callback invoked when the OK button is clicked."""
		# In theory, this would be a good place to validate user input
		# before committing changes.  In practice...
		self.window.hide()
		gtk.main_quit()
		self.estat = False
