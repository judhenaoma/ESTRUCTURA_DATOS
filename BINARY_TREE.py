class Node:
    def __init__(self, elm):
        self.elm = elm
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.size = 0
        self.root = None
    
    def insert_recursive(self, node, elm):
        if node is None:
            new_node = Node(elm)
            if self.size == 0:
                self.root = new_node
            self.size += 1
            return new_node
        if elm < node.elm:
            node.left = self.insert_recursive(node.left, elm)
        else:
            node.right = self.insert_recursive(node.right, elm)
        return node

    def findMin(self, node):
        current = node
        while(current.left is not None):
            current = current.left
        return current

    def delete_recursive(self, root, elm):
        if root is None:
            return root
        if elm < root.elm:
            root.left = self.delete_recursive(root.left, elm)
        elif(elm > root.elm):
            root.right = self.delete_recursive(root.right, elm)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.findMin(root.right)
            root.elm = temp.elm
            root.right = self.delete_recursive(root.right, temp.elm)
        return root
    
    def search_recursive(self, root, elm):
        if root is None or root.elm == elm:
            return root
        if elm < root.elm:
            return self.search_recursive(root.left, elm)
        else:
            return self.search_recursive(root.right, elm)

    # User functions 
    def insert(self, elm):
        self.insert_recursive(self.root, elm)
    
    def delete(self, elm):
        self.size -= self.search(elm)
        self.root = self.delete_recursive(self.root, elm)

    def search(self, elm):
        return self.search_recursive(self.root, elm) != None        

