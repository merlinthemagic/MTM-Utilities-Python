
import re
from .processing import Processing

class Initialization(Processing):

	def __init__(self):
		self._args			= [];
		super().__init__()
		
	def setArgs(self, list=[]):
		self._args			= list;
		return self;
	
	def getArgs(self):
		return self._args;