class Base:
	
	def __init__(self):
		if type(self) is Base:
			raise TypeError("Base is abstract and cannot be instantiated directly");

		self._s				= {};
		self._Facts			= None;
		self._isInit		= False;
		self._isTerm		= False;
		self._debugObj		= False;
				
	def isInit(self):
		return self._isInit;

	def isTerm(self):
		return self._isTerm;

	def getDebug(self):
		return self._debugObj["enabled"];

	def setDebugObj(self, obj):
		self._debugObj	= obj;
		return self;

	def getFacts(self):
		if self._Facts is None:
			from ..Facts import Facts
			self._Facts			= Facts;
		return self._Facts;