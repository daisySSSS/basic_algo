from tree_tranverse import inorder_tranverse_recursive,inorder_tranverse_iterative,preorder_tranverse_recursive,preorder_tranverse_iterative,postorder_tranverse_recursive,postorder_tranverse_iterative

class Tree:
    def __init__(self, left=None, right=None, value=None):
        self.left = left
        self.right = right
        self.value = value

root = Tree(value=0)
root.left = Tree(value=1)
root.right = Tree(value=2)
root.left.left = Tree(value=3)
root.left.right = Tree(value=4)
root.right.left = Tree(value=5)
root.right.right = Tree(value=6)

print(inorder_tranverse_recursive(root)==inorder_tranverse_iterative(root))
print(preorder_tranverse_recursive(root)==preorder_tranverse_iterative(root))
print(postorder_tranverse_recursive(root)==postorder_tranverse_iterative(root))