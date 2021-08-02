class Tree:
    def __init__(self, left=None, right=None, value=None):
        self.left = left
        self.right = right
        self.value = value
        
def inorder_tranverse_recursive(root):
    if root.left:
        inorder_tranverse_recursive(root.left)
    print(root.value)
    if root.right:
        inorder_tranverse_recursive(root.right)

def inorder_tranverse_iterative(root):
    node = root
    stack = []
    while 1:
        if node:
            stack.append(node)
            node = node.left
        elif stack:
            node = stack.pop()
            print(node.value)
            node = node.right
        else: break

def preorder_tranverse_recursive(root):
    print(root.value)
    if root.left:
        preorder_tranverse_recursive(root.left)   
    if root.right:
        preorder_tranverse_recursive(root.right)

def preorder_tranverse_iterative(root):
    node = root
    stack = []
    while 1:
        if node:
            print(node.value)
            stack.append(node)
            node = node.left
        elif stack:
            node = stack.pop()
            node = node.right
        else: break

def postorder_tranverse_recursive(root):
    if root.left:
        postorder_tranverse_recursive(root.left)   
    if root.right:
        postorder_tranverse_recursive(root.right)
    print(root.value)

def postorder_tranverse_iterative(root):
    node = root
    stack = []
    while 1:
        if node:
            stack.append(node)
            stack.append(node)
            node = node.left
        elif stack:
            node = stack.pop()
            if stack and stack[-1]==node:
                node = node.right
            else:
                print(node.value)
                node=None
            
        else: break