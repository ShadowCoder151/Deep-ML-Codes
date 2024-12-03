class Value:
	def __init__(self, data, _children=(), _op=''):
		self.data = data
		self.grad = 0
		self._backward = lambda: None
		self._prev = set(_children)
		self._op = _op
	def __repr__(self):
		return f"Value(data={self.data}, grad={self.grad})"

	def __add__(self, other):
		 # Implement addition here
		other = other if isinstance(other, Value) else Value(other)
		out = Value(self.data + other.data, (self, other), '+')
		
		def _backward():
			self.grad += out.grad
			other.grad += out.grad
		out._backward = _backward
		return out

	def __mul__(self, other):
		# Implement multiplication here
		other = other if isinstance(other, Value) else Value(other)
		out = Value(self.data * other.data, (self, other), '+')

		def _backward():
			self.grad += out.grad * other.data
			other.grad += out.grad * self.data
		out._backward = _backward
		return out

	def relu(self):
		# Implement ReLU here
		# other = other if isinstance(other, value) else Value(other)
		out = Value(max(0, self.data), (self, ), 'ReLU')
		
		def _backward():
			self.grad += out.grad * (out.data > 0)
			# other.grad += out.grad
		out._backward = _backward
		return out

	def backward(self):
		# Implement backward pass here
		topo = []
		visited = set()
		
		def topo_sort(v):
			if v not in visited:
				visited.add(v)
				for ch in v._prev:
					topo_sort(ch)
				topo.append(v)
		
		topo_sort(self)
		
		self.grad = 1
		for node in reversed(topo):
			node._backward()

a = Value(2);b = Value(3);c = Value(10);d = a + b * c  ;e = Value(7) * Value(2);f = e + d;g = f.relu()  
g.backward()
print(a,b,c,d,e,f,g)