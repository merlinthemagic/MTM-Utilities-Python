from .base import Base
import threading
from .Tools.time import Time as _Time

class Tools(Base):
	
	def __init__(self):
		super().__init__();
		self._timeLock	= threading.Lock();
		
	def getTime(self):
		key		= "getTime";
		if key not in self._s:
			with self._timeLock:
				if key not in self._s:
					self._s[key] = _Time();
					
		return self._s[key];