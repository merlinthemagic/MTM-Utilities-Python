from typing import List
from ..Task.alpha import Alpha as _taskObj
from .initialization import Initialization

class Alpha(Initialization):

	def __init__(self):
		super().__init__();

		self._max_workers: int					= 4;
		self._heap: List[_taskObj]				= [];
		self._allStop							= self.getFacts().getProcess().getAllStop();

	def getMaxWorkers(self) -> int:
		return self._max_workers

	def setMaxWorkers(self, max_workers: int):
		self._max_workers	= max_workers;
		return self

	def getHeapSize(self):
		with self._lock:
			return len(self._heap)

	def getTask(self):
		return _taskObj();

	

	

	