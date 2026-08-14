import threading
from ....base import Base

class Zulu(Base):
	
	def __init__(self):
		
		super().__init__();
		self._termLock	= threading.Lock();
		
	
	def terminate(self):
		with self._termLock:
			if not self._isTerm:
				self._isTerm	= True;