class Node(object):
	def __init__(self,val):
		self.val = val
		self.right,self.left = None, None

class BTree(object):
	def __init__(self):
		self.root = None

	def insert(self,data):
		if self.root is None:
			self.root = Node(data)
		else:
			self._put(data,self.root)

	def _put(self,data,root):
		nodeQueue = []
		nodeQueue.append(root)
		while nodeQueue:
			node = nodeQueue[0]
			nodeQueue.remove(node)
			if node.left is None:
				node.left = Node(data)
				break
			else:
				nodeQueue.append(node.left)
			if node.right is None:
				node.right = Node(data)
				break
			else:
				nodeQueue.append(node.right)

if __name__ == '__main__':
	obj = BTree()
	obj.insert("10")
	obj.insert("20")
	obj.insert("30")
	obj.insert("40")
	obj.insert("50")
	# print (obj.root.val)
	print (obj.root.left.val)
	# print (obj.root.right.val)
