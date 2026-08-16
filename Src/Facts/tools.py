from .base import Base
import threading
from .Tools.time import Time as _Time
from .Tools.lock import Lock as _Lock

class Tools(Base):
	
	def __init__(self):
		super().__init__();
		self._timeLock	= threading.Lock();
		self._lockLock	= threading.Lock();
		
	def getTime(self):
		key		= "getTime";
		if key not in self._s:
			with self._timeLock:
				if key not in self._s:
					self._s[key] = _Time();
					
		return self._s[key];
		
	def getLock(self):
		key		= "getLock";
		if key not in self._s:
			with self._lockLock:
				if key not in self._s:
					self._s[key] = _Lock();
					
		return self._s[key];