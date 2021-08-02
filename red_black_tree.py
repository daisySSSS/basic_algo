from binary_search_tree import BinarySearchTree


class RedBlackTreeNode():
    def __init__(self, val = None, left = None, right = None, parent = None, color = 'black'):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
        self.color = color

def is_redblacktree(x):
    if not x:
        return True
    if x.root.color != 'black':
        print('property 2 not satisfied. (root not black)')
        return False
    stack = [[x.root, 1]]
    black_height_list = []
    while stack:
        node, black_height = stack.pop()
        if node.val == None:
            if node.color == 'black':
                black_height_list.append(black_height)
            else: 
                print('property 3 not satisfied. (leaf not black.)')
                return False
        else:
            if node.color not in ['red', 'black']:
                print('property 1 not satisfied. (only red and black allowed)')
                return False
            if node.color=='red':
                if node.left and node.left.color != 'black':
                    print('property 4 not satisfied. (red parent has black children)')
                    return False
                if node.right and node.right.color != 'black':
                    print('property 4 not satisfied. (red parent has black children)')
                    return False
            if node.left:
                if node.left.color == 'black':
                    stack.append([node.left, black_height+1])
                else: stack.append([node.left, black_height])
            if node.right:
                if node.right.color == 'black':
                    stack.append([node.right, black_height+1])
                else: stack.append([node.right, black_height])
            if not node.left and not node.right:
                print('property 3 not satisfied. (leaf not black.)')
                return False
    if len(set(black_height_list))!=1:
        print(black_height_list)
        print('property 5 not satisfied. (equal black height for all branches)')
        return False
    return True
def is_equal_tree(x,y):
    if not x and not y:
        return True
    elif (x and not y) or (y and not x):
        return False

    stack_x = [x]
    stack_y = [y]
    flag = 0
    while stack_x and stack_y:
        x = stack_x.pop()
        y = stack_y.pop()
        if x.val != y.val:
            flag = 1
            break
        if x.right and y.right:
            stack_x.append(x.right)
            stack_y.append(y.right)
        elif (x.right and not y.right) or (not x.right and y.right):
            flag = 1
            break
        if x.left and y.left:
            stack_x.append(x.left)
            stack_y.append(y.left)
        elif (x.left and not y.left) or (not x.left and y.left):
            flag = 1
            break    
    if flag:
        return False
    else:
        return True    

class RedBlackTree(BinarySearchTree):
    def __init__(self, root=None):
        self.root = root
        self.nil = RedBlackTreeNode()
        self.root.parent = self.nil

    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if is_equal_tree(y.left,self.nil):
            y.left.parent = x
        y.parent = x.parent
        if is_equal_tree(x.parent,self.nil):
            self.root = y
        elif is_equal_tree(x,x.parent.left):
            x.parent.left = y
        else: is_equal_tree(x.parent.right,y)
        y.left = x
        x.parent = y

    def _right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else: x.parent.right = y
        y.right = x
        x.parent = y
        return y

    def _insert_fixup(self, z):
        while z.parent.color == 'red':
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == 'red':
                    z.parent.color = 'black'
                    y.color = 'black'
                    z.parent.parent.color = 'red'
                    z = z.parent.parent
                elif z == z.parent.right:
                    z = z.parent
                    self._left_rotate(z)
                else:
                    z.parent.color = 'black'
                    z.parent.parent.color = 'red'
                    self._right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == 'red':
                    z.parent.color = 'black'
                    y.color = 'black'
                    z.parent.parent.color = 'red'
                    z = z.parent.parent
                elif z == z.parent.left:
                    z = z.parent
                    self._right_rotate(z)
                else:
                    z.parent.color = 'black'
                    z.parent.parent.color = 'red'
                    self._left_rotate(z.parent.parent)

    def insert(self, z):
        x = self.root
        y = self.nil

        while not is_equal_tree(x,self.nil):
            y = x
            if z.val < x.val:
                x = x.left
            else:
                x = x.right
        if is_equal_tree(y,self.nil):
            self.root = z
        elif z.val < y.val:
            y.left = z
        else: y.right = z
        z.left = self.nil
        z.right = self.nil
        z.color = 'red'
        z.parent = y
        self._insert_fixup(z)