
class CampsCerc:
	"""
	Classe que defineix els camps que s'han d'usar a una cerca
	"""
	def __init__(self):
	
		self.__camps= []
		self.__etiqueta = {}
		self.__tipus = {}
		self.__attributs = {}
		self.__camps_cerca = []

	def posa_camp(self, pCamp, pTipus, pEtiqueta, pCerca=False):
		self.__camps.append(pCamp)
		self.__etiqueta[pCamp] = pEtiqueta
		self.__tipus[pCamp] = pTipus
		if (pCerca):
			self.__camps_cerca.append(pCamp)
	
	def lleva_camp(self, pCamp):
		try:
			self.__camps.remove(pCamp)
			del self.__tipus[pCamp]
			del self.__etiqueta[pCamp]
			if (pCamp in self.__camps_cerca):
				self.__camps_cerca.remove(pCamp)
		
		except:
			return
	
	def obte_tipus(self):
		return [self.__tipus[x] for x in self.__camps]
	
	def obte_camps(self):
		return self.__camps

	def obte_etiquetes(self):
		return [self.__etiqueta[x] for x in self.__camps]

	def obte_etiqueta(self, pCamp):
		return self.__etiqueta[pCamp]

	def obte_camps_cerca(self):
		return self.__camps_cerca

