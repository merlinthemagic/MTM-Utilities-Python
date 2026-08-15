import time
from .processing import Processing

class Initialization(Processing):
	
	def __init__(self):
		
		super().__init__();

	def initialize(self):
		
		if not self._isInit:
			
			try:

				if self.getName() is None:
					raise ValueError("name must be set before initialize()");
				if self.getFunction() is None:
					raise ValueError("function must be set before initialize()");
				if self.getInterval() is None or self.getInterval() <= 0:
					raise ValueError("interval must be a positive number");
				if self.getSeq() is None:
					raise ValueError("seq must be set before initialize() (assigned by the scheduler)");

				if self.getNextRun() is None:
					self.setNextRun(time.monotonic() + 1); ##all tasks run right away to start, then the interval kicks in

				self._isInit	= True;

			except Exception as e:
				#logging needed
				self.terminate();
				if self.getDebug():
					raise e;