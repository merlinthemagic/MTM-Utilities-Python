from ..base import Base
import threading
from ...Tools.Time.Epoch.alpha import Alpha as _Epoch

class Time(Base):
	
	def __init__(self):
		super().__init__();
		self._epochLock		= threading.Lock();
		
	def getEpoch(self):
		key		= "getEpoch";
		if key not in self._s:
			with self._epochLock:
				if key not in self._s:
					self._s[key] = _Epoch();
#					
		return self._s[key];