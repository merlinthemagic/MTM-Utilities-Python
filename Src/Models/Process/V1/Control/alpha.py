import heapq, threading
from typing import List
from ..Task.alpha import Alpha as _taskObj
from .initialization import Initialization

class Alpha(Initialization):

	def __init__(self):
		super().__init__();

		self._max_workers: int					= 4;
		self._heap: List[_taskObj]				= [];
		self._allStop							= self.getFacts().getProcess().getAllStop();
		self._lock								= threading.Lock();

	def getMaxWorkers(self) -> int:
		return self._max_workers

	def setMaxWorkers(self, max_workers: int):
		self._max_workers	= max_workers;
		return self

	def getHeapSize(self):
		with self._lock:
			return len(self._heap)


	##Tasks
	def getTask(self):
		rObj		= _taskObj();
		rObj.setControl(self);
		return rObj;
	
	def registerTask(self, taskObj):
		if taskObj.getSeq() is None:
			taskObj.setSeq(next(self._counter));

		if not taskObj.isInit():
			taskObj.initialize();

		with self._lock:
			heapq.heappush(self._heap, taskObj);

		return self;
	
	def removeTask(self, taskObj):
		with self._lock:
			try:
				self._heap.remove(taskObj);
				heapq.heapify(self._heap)  # restore heap invariant, O(n)
			except ValueError:
				pass  # wasn't in the heap
		return self;

	

	