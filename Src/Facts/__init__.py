
from .processes import Processes as _Processes
from .tools import Tools as _Tools
from .test import Test as _Test

class Facts:
	
	_s = {}

	@classmethod
	def getProcesses(cls):
		if "getProcesses" not in cls._s:
			cls._s["getProcesses"] = _Processes();
		return cls._s["getProcesses"];

	@classmethod
	def getTools(cls):
		if "getTools" not in cls._s:
			cls._s["getTools"] = _Tools();
		return cls._s["getTools"];
		
	@classmethod
	def getTest(cls):
		if "getTest" not in cls._s:
			cls._s["getTest"] = _Test();
		return cls._s["getTest"];