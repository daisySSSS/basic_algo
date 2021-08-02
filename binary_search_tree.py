# binary_search_tree
# median
class Node():
    def __init__(self, val, left = None, right = None, parent = None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent


class BinarySearchTree():
    def __init__(self, root=None):
        self.root = root
    
    def print_tree(self):
        x = self.root
        queue = [x]
        while queue:
            cur = queue.pop(0)
            tmp = []
            if cur.left:
                queue.append(cur.left)
                tmp.append(cur.left.val)
            else:
                tmp.append('nil')
            if cur.right:
                queue.append(cur.right)
                tmp.append(cur.right.val)
            else:
                tmp.append('nil')
            print(cur.val, tmp)
            
    def search(self, num):
        x = self.root
        while x:
            if num < x.val:
                x = x.left
            elif num == x.val:
                return x
            else:
                x = x.right   

    def insert(self, num):
        x = self.root
        y = None
        while x:
            if num < x.val:
                y = x
                x = x.left
            else:
                y = x
                x = x.right
        if not y:
            self.root = Node(num)
        else:
            if num < y.val:
                y.left = Node(num)
                y.left.parent = y
            else:
                y.right = Node(num) 
                y.right.parent = y    

    def successor(self, x):
        if not x:
            x = self.root
        if x.right:
            return self.min(x.right)
        else:
            y = x.parent
            while y and x == y.right:
                x = y
                y = x.parent
            return y


    def delete(self, x):
        if not x.left:
            self.transplant(x,x.right)
        if not x.right:
            self.transplant(x, x.left)
        else:
            y = self.min(x.right)
            if x.right != y:
                self.transplant(y, y.right)
                y.right = x.right
                y.right.parent = y
            self.transplant(x, y)
            y.left = x.left
            y.left.parent = y

    def transplant(self, x, y):
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        if y != None:
            y.parent = x.parent


    def min(self, x=None):
        if not x:
            x = self.root
        while x.left:
            x = x.left
        return x

    def max(self, x=None):
        if not x:
            x = self.root
        while x.right:
            x = x.right
        return x
