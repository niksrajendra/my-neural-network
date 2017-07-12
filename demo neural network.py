import numpy as np
import layers

class model:
	def __init__(self):
		self.layer = []

	def add(self,string):
		self.layer.append(string)
		print self.layer

	def fit(self,inputs,outputs):
		pass

	def compile(self):
		for layers in self.layer:
			pass 

epoch = 100

X = np.array([[0,0,1],[0,1,1],[1,0,1],[1,1,1]])
Y = np.array([[0,1,1,0]]).T
kernal1 = 2*np.random.random((3,4)) - 1
kernal2 = 2*np.random.random((4,1)) - 1

test = model()
test.add('sigmoid')
test.add('tanh')
test.add('linear')

'''for i in range(epoch):
	a = sigmoid(np.dot(X,kernal1))
	b = sigmoid(np.dot(a,kernal2))
	gradient1 = b.backward(Y-b)
	gradient2 = a.backward(gradient1)
	kernal1 +=
	kernal2 += '''
