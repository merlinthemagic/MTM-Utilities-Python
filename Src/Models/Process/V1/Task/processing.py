import time
from .zulu import Zulu

class Processing(Zulu):
	
	def __init__(self):
		
		super().__init__();
	
	def process(self):
		# only run once the object has actually been initialized
		# (previously this checked `not self._isInit`, which is inverted)
		if self._isInit:
			
			try:

				start		= time.monotonic();
				self.getFunction()(self);
				elapsed		= time.monotonic() - start;

				if elapsed > self.getTimeout():
					#logging needed - collector exceeded its timeout budget
					pass

			except Exception as e:
				#logging needed
				if self.getDebug():
					raise e;