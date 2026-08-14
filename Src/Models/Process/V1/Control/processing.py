import heapq, time
from .zulu import Zulu

class Processing(Zulu):
	
	def __init__(self):
		
		super().__init__();
		
	
	def processLoop(self):
		while not self._allStop.is_set():
			self.process();
			
	def process(self):
		
		if self._isInit:
			try:
				with self._lock:
					if not self._heap:
						sleep_for	= 1.0;
					else:
						sleep_for	= self._heap[0].getNextRun() - time.monotonic();

				if sleep_for > 0:
					# wait, but wake early if terminate() fires
					self._allStop.wait(timeout=sleep_for);
					return;

				with self._lock:
					taskObj	= heapq.heappop(self._heap);


				taskObj.setNextRun(taskObj.getNextRun() + taskObj.getInterval());

				with self._lock:
					heapq.heappush(self._heap, taskObj);

				self._pool.submit(taskObj.process);

			except Exception as e:
				#logging needed
				if self.getDebug():
					raise e;
			