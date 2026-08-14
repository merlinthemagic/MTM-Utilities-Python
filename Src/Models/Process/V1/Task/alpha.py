from typing import Callable, Optional
from .initialization import Initialization

class Alpha(Initialization):

	def __init__(self):
		super().__init__();

		self._next_run: Optional[float]				= None
		self._seq: Optional[int]					= None
		self._name: Optional[str]					= None
		self._interval: Optional[float]				= None
		self._fn: Optional[Callable[[], None]]		= None
		self._timeout: float						= 10.0

	# --- next_run ---
	def getNextRun(self) -> float:
		return self._next_run;

	def setNextRun(self, next_run: float):
		self._next_run	= next_run;
		return self

	def getSeq(self) -> int:
		return self._seq;

	def setSeq(self, seq: int):
		self._seq	= seq;
		return self

	def getName(self) -> str:
		return self._name;

	def setName(self, name: str):
		self._name	= name;
		return self

	def getInterval(self) -> float:
		return self._interval;

	def setInterval(self, interval: float):
		self._interval	= interval;
		return self

	def getFunction(self) -> Callable[[], None]:
		return self._fn;

	def setFunction(self, fn: Callable[[], None]):
		self._fn	= fn;
		return self

	def getTimeout(self):
		return self._timeout;

	def setTimeout(self, timeout: float):
		self._timeout	= timeout;
		return self;

	def __lt__(self, other):
		# heapq only ever needs <, not the full comparison suite
		return (self._next_run, self._seq) < (other._next_run, other._seq);

	def __repr__(self) -> str:
	    next_run = f"{self._next_run:.2f}" if self._next_run is not None else "None"
	    return f"TaskObj(name={self._name!r}, next_run={next_run})"
		
		