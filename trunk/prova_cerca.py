#!/usr/bin/env python
# -*- coding: UTF8 -*-

# Python module prova.py
# Autogenerated from prova
# Generated on Thu Sep  1 12:12:14 2005

# Warning: Do not modify any context comment such as #--
# They are required to keep user's code

import FrmCercador
from  CampsCerc import *


camps = CampsCerc()
camps.posa_camp( "ID", int, "Codi", False )
camps.posa_camp( "DNI", int, "D.N.I.", False )
camps.posa_camp( "NOM", str, "Nom", True )
camps.posa_camp( "LLINATGES", str, "Cognoms", True )
camps.posa_camp( "TELEFON", int, "Telèfon", True )



taula = "CLIENT"
base = { "nom_base_dades" : "gjdb.fdb", "host" : "localhost", 
                "usuari" : "sysdba", "password" : "coder666" }
  
cerc = FrmCercador.Cercador(camps, taula, base )
res = cerc.run()
 
print res
 
 



