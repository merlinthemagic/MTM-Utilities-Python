from .base import Base

from ..Models.Processes.Child.alpha import Alpha as _ChildAlpha

class Processes(Base):
	
	def getChild(self, argList=[]):
		rObj	= _ChildAlpha();
		rObj.setArgs(argList);
		return rObj;
