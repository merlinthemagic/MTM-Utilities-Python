from ..base import Base
import threading
from ...Tools.Lock.FailSafe.alpha import Alpha as _FailSafe

class Lock(Base):
	
	def __init__(self):
		super().__init__();
		self._failSafeLock		= threading.Lock();
		
	def getFailSafe(self):
		key		= "getFailSafe";
		if key not in self._s:
			with self._failSafeLock:
				if key not in self._s:
					self._s[key] = _FailSafe();
#					
		return self._s[key];