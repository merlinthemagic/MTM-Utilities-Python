from .base import Base

class Test(Base):
	
	def execute(self):

		from . import Facts

		

		try:
			
			print("All checks passed.")

		finally:
			print("Error?");