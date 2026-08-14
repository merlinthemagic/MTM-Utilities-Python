from .process import Process as _Process
from .tools import Tools as _Tools
from .test import Test as _Test

class Facts:
	
	_s		= {};
	
	@classmethod
	def getProcess(cls):
		key		= "getProcess";
		if key not in cls._s:
			cls._s[key] = _Process();
		return cls._s[key];

	@classmethod
	def getTools(cls):
		key		= "getTools";
		if key not in cls._s:
			cls._s[key] = _Tools();
		return cls._s[key];
		
	@classmethod
	def getTest(cls):
		key		= "getTest";
		if key not in cls._s:
			cls._s[key] = _Test();
		return cls._s[key];