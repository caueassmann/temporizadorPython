from os.path import dirname, realpath
from json import dump, load

class JsonClass():

	def __init__(self):
		self.path = dirname(realpath(__file__)) + '/'
	
	def lerJson(self,file):
		with open(self.path +  file,"r") as f:
			data = load(f)
		return data

	def gravarJson(self, file, info):
		with open(file, "w") as f:

			dump(info, f, indent=7, separators = (',',': '))
