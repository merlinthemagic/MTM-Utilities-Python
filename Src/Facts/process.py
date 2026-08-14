import threading, signal
from ..Models.Process.V1.Control.alpha import Alpha as _ctrlV1
from .base import Base

class Process(Base):

	def __init__(self):
		super().__init__();
		
		self._termLock	= threading.Lock();
		self._allStop	= threading.Event();
		signal.signal(signal.SIGINT, self.handleSigint);
		
	def getV1(self):
		return _ctrlV1();
		
	def getAllStop(self):
		##all threads should honor this stop
		return self._allStop;
		
	##termination logic
	def handleSigint(self, signum, frame):
		self._allStop.set();
	
	def terminate(self):
		with self._termLock:
			if not self._isTerm:
				self._allStop.set();
				self._isTerm	= True;