#!/usr/bin/env python
# -*- coding: UTF8 -*-
#
# Python module libgesjo.py
# Generated on Tue Sep  6 19:27:17 2005
#


import BaseDades as bdd


class gesjo:
    """
    Llibreria que conté tota la lògica de l'aplicació.
    """
    def __init__(self):
        import ConfigParser
        import os 
        self.config = ConfigParser.ConfigParser() 
        self.config.readfp( open( "config.ini" ) )
        
        if not self.config.has_section( "CONNEXIO" ):
            # No hi ha configuració, per tant not feim res, tornam Fals
            print "ERROR! No s'ha trobat la configuració."
            raise Exception( "FALTEN PARAMETRES DE CONNEXIO" )
        self.connexio = dict( self.config.items( "CONNEXIO" ) )
        
        self.BD = bdd.BaseDades()
        fitxerbase  =  os.path.normpath( os.path.join( os.sep.join( os.getcwd().split( os.sep ) ), self.connexio["base"] ) )
        try:
            self.BD.connexio(host=self.connexio["servidor"], base=fitxerbase, usuari=self.connexio["usuari"], clau=self.connexio["password"] )
        except:
            print "No s'ha pogut connectar a la base de dades. "
            raise Exception("ERROR DE CONNEXIO")
        
        
        
        
        
if __name__ == "__main__":
    g = gesjo()
           
        
        