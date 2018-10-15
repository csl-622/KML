class EditDataStructure:

	def __init__(self):
		self.del_ = {}
		self.map_ = {}

	def del_add(self, ind, word):
		self.del_[ind] = word

	def map_add(self, ind, word):
		self.map_[ind] = word

	def get_del(self):
		return self.del_

	def get_map(self):
		return self.map_



class GitMechanism:

	def __init__(self, str):
		self.original = str
		self.map = {}
		self.mapper()
		self.ind = [(i+1) for i in range(len(self.original.split(" ")))]
		self.revision = []
		self.current = self.original

	def getOriginal(self):
		return self.original

	def get_revision(self):
		return self.revision

	def getInd(self):
		return self.ind

	def mapper(self):
		for i, word in enumerate(self.original.split(" ")):
			self.map[i+1] = word

	def getMap(self):
		return self.map

	def getCurrent(self):
		return self.current

	def modify(self, stri):
		curr = self.current.split(" ")
		edit = stri.split(" ")
		#print("CURR: ", curr)
		#print("EDIT: ", edit)
		eds = EditDataStructure()
		min_len = min(len(curr), len(edit))
		for i in range(min_len):
			if(curr[i] != edit[i]):
				eds.map_add(i, curr[i])
		for i, word in enumerate(range(min_len, len(edit))):
			eds.map_add(i, word)
		self.revision.append(eds)





g = GitMechanism("My name is Nitin Gandhi")
print("Original: ", g.getOriginal())
print("Original Index: ", g.getInd())
print("Current: ", g.getCurrent())
print(g.getMap())
g.modify("My name is Nitin Gandhi and I am Cool")

print(g.get_revision()[0].map_)
