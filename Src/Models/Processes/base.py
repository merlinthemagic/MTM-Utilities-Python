
import uuid

class Base:

	def __init__(self):
		if type(self) is Base:
			raise TypeError("Base is abstract and cannot be instantiated directly")
		
		self._guid			= None
		self._is_init		= False
		self._is_term		= False
		self._init_active	= False
		self._term_active	= False
		
	def getGuid(self):
		if self._guid is None:
			self._guid = str(uuid.uuid4())
		return self._guid