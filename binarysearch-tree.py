class Node:
    
    def __init__ (self, val):
        self.val   = val
        self.right = None
        self.left  = None

class binary_tree:
    
    def __init__(self):
      self.root = None
    
    # Add Node
    def add(self, val):
        if (self.root == None):
            self.root = Node(val)
        else:
            self.add_node(self.root, val)
    
    # Node should not be None
    def add_node(self, node, val):
        if (node.val < val):
            self.add_right(node, val)
        else:
            self.add_left(node, val)
    
    def add_right(self, node, val):
        if (node.right == None):
            node.right = Node(val)
        else:
            self.add_node(node.right, val)
    
    def add_left(self, node, val):
        if (node.left == None):
            self.left = Node(val)
        else:
            self.add_node(node.left, val)
    
    def printTree(self):
        if (self.root == None):
            print("diagrph structs {\nnode [shape=record]:")
            self._printLabel(self.root)
            self._printTree(self.root)
            print("}")
    
    def _printLabel(self, node):
        if (node != None):
            print("struct" + str(node.val) + "[Label='<f0>|" + str(node.val) + "|<f1>'];")
            self._printLabel(node.left)
            self._printLabel(node.right)
            
    def _printTree(self, node):
        if (node != None):
            if (node.left != None):
                print("struct" + str(node.val) + ":f0 -> struct" + str(node.left.val))
            if (node.right != None):
                print("struct" + str(node.val) + ":f1 -> struct" + str(node.right.val))
            self._printTree(node.left)
            self._printTree(node.right)

tree = binary_tree()
tree.add(3)
tree.add(0)
tree.add(2)
tree.add(4)
tree.add(8)
tree.printTree()