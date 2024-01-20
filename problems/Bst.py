class TreeNode:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self.insert_recursive(self.root, key)

    def insert_recursive(self, node, key):
        if node == None:
            return TreeNode(key)

        if key < node.key:
            node.left = self.insert_recursive(node.left, key)       

        elif key > node.key:
            node.right = self.insert_recursive(node.right,key)

        return node

    def delete(self, key):
        self.root = self.del_recursive(self.root, key)

    def del_recursive(self, node, key):
        if node is None:
            return node

        if key < node.key:
            node.left = self.del_recursive(node.left, key)
        elif key > node.key:
            node.right = self.del_recursive(node.right, key)
        else:
            # case 1 : no child or one child (leaf nodes).
            if node.left == None:
                return node.right
            elif node.right == None:
                return node.left

            node.key = self.find_min_key(node.right)
            node.right = self.del_recursive(node.right, node.key)
        return node    

    def find_min_key(self, node):
        current = node
        while current.left != None:
            current = current.left
        return current.key                    

    def inorder_traversal(self):
        result = []
        stack = []
        current = self.root

        while current is not None or len(stack) > 0:
            while current is not None:
                stack.append(current)
                current = current.left

            current = stack.pop()
            result.append(current.key)
            current = current.right

        return result



bst = BinarySearchTree()

# Insert elements
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(2)
bst.insert(4)
bst.insert(6)
bst.insert(8)

print("Inorder Traversal of BST:", bst.inorder_traversal())

# Delete elements
bst.delete(3)
bst.delete(7)

print("Inorder Traversal after Deletion:", bst.inorder_traversal())