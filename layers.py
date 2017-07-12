class sigmoid:
	def __init__(self,x):
		self.x = x

	def forward(self):
		return 1/(1+np.exp(-self.x))

	def backword(self,y):
		return np.dot(y,1-y)

class tanh:
	def __init__(self,x):
		self.x = x

	def forward(self):
		return 2/(1+np.exp(-2,self.x)) - 1

	def backward(self,y):
		return 1 - np.dot(y,y)

class linear:
	def __init__(self,x):
		self.x = x

	def forward(self):
		return self.x

	def backward(self,y):
		return y
