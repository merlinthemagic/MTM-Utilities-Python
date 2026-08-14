import itertools, threading
from typing import List, Optional
from concurrent.futures import ThreadPoolExecutor
from .processing import Processing

class Initialization(Processing):
	
	def __init__(self):
		
		super().__init__();
		self._counter										= itertools.count();
		self._pool: Optional[ThreadPoolExecutor]			= None;

	def initialize(self):
		if not self._isInit:
			
			try:
				
				if self._max_workers is None or self._max_workers <= 0:
					raise ValueError("max_workers must be a positive number");

				self._pool		= ThreadPoolExecutor(max_workers=self._max_workers);
				runThread		= threading.Thread(target=self.processLoop, args=());
				runThread.start();
				self._isInit	= True;
				
			except Exception as e:
				#logging needed
				self.terminate();
				if self.getDebug():
					raise e;

				
	