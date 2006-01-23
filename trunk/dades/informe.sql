select a.id, c.nom, c.LLINATGES, c.TELEFON, m.NOM as marca, a.model, a.TREBALL,
a.DATA_ENTRADA, a.DATA_ENTREGA, a.PVP, me.NOM as mecanic, t.NOM as taller, me.TELEFON
from ARREGLO a, client c, marca m, mecanic me, taller t
where a.CLIENT_ID = c.ID and a.MARCA_ID = m.ID and a.MECANIC_ID = me.ID
and me.TALLER_ID = t.ID