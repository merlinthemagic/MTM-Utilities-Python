import time
from .zulu import Zulu

class Processing(Zulu):
	
	def __init__(self):
		
		super().__init__();
		self._isIdle	= True;
	
	def getIdle(self):
		return self._isIdle;
		
	def setIdle(self, bool):
		self._isIdle 	= bool;
		return self;
		
	def process(self):
		# only run once the object has actually been initialized
		# (previously this checked `not self._isInit`, which is inverted)
		if self._isInit:
			
			try:
				
				start			= time.monotonic();	
				self.getFunction()(self);
				self.setIdle(True);
				elapsed			= time.monotonic() - start;

				if elapsed > self.getTimeout():
					#logging needed - task exceeded its timeout budget
					pass;

			except Exception as e:
				#logging needed
				self.setIdle(True);
				self.getControl().exceptionCb(e, self);
				
				if self.getDebug():
					elapsed			= time.monotonic() - start;
					print(e);
					print(self.getName()+" ran exception long: "+str(round(elapsed - self.getTimeout())));
					pass;
					
				
				
				if self.getDebug():
					raise e;