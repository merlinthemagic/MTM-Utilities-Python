import threading, signal, os, time
from ..Models.Process.V1.Control.alpha import Alpha as _ctrlV1
from .base import Base

class Process(Base):

	def __init__(self):
		super().__init__();
		
		##how long to sleep after all stop is fired, before triggering sy.exit
		self._exitWait	= 3;
		self._termLock	= threading.Lock();
		self._allStop	= threading.Event();
		self._debug		= {"enabled": False};
		signal.signal(signal.SIGINT, self.handleSigint);
		
	def getV1(self):
		rObj	= _ctrlV1();
		rObj.setDebugObj(self._debug);
		return rObj;
	
	def enableDebug(self):
		self._debug["enabled"]	= True;
		return self;
		
	def getDebug(self):
		return self._debug["enabled"];
		
	def getDebugObj(self):
		return self._debug;
			
	def getAllStop(self):
		##all threads should honor this stop
		return self._allStop;
		
	##termination logic
	def handleSigint(self, signum, frame):
		self.terminate();
		
	
	def terminate(self):
		if not self._isTerm:
			with self._termLock:
				if not self._isTerm:
					self._isTerm	= True;
					self._allStop.set();
					time.sleep(self._exitWait);
					
					##force exit. This is not amazing logic but 
					##Because the handler swallows the signal and if there a loop running not using the allStop event it will keep running
					os._exit(1);