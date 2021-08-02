import pytest

from red_black_tree import RedBlackTreeNode, RedBlackTree, is_equal_tree, is_redblacktree

def getTree1():
    # Tree 1
    #       1
    #     /    \
    #   0       3
    #          /  \
    #         2    4
    x = RedBlackTreeNode(val=1)
    y = RedBlackTreeNode(val=3, color='red')
    x.left = RedBlackTreeNode(val=0)
    x.left.left = RedBlackTreeNode()
    x.left.right = RedBlackTreeNode()
    x.right = y
    y.parent = x
    y.left = RedBlackTreeNode(val=2)
    y.right = RedBlackTreeNode(val=4)
    y.left.left = RedBlackTreeNode()
    y.left.right = RedBlackTreeNode()
    y.right.left = RedBlackTreeNode()
    y.right.right = RedBlackTreeNode()
    tree = RedBlackTree(root=x)
    return tree

def getTree2():
    # Tree2
    #        3
    #       /  \
    #     1     4
    #    / \
    #   0   2
    x = RedBlackTreeNode(val=1, color='red')
    y = RedBlackTreeNode(val=3)
    x.left = RedBlackTreeNode(val=0)
    x.right = RedBlackTreeNode(val=2)
    x.left.left = RedBlackTreeNode()
    x.left.right = RedBlackTreeNode()
    x.right.left = RedBlackTreeNode()
    x.right.right = RedBlackTreeNode()
    y.right = RedBlackTreeNode(val=4)
    y.right.left = RedBlackTreeNode()
    y.right.right = RedBlackTreeNode()
    y.left = x
    x.parent = y
    tree = RedBlackTree(root=y)
    return tree

def getTree3():
    # Tree3
    #           5
    #         /
    #       1
    #     /    \
    #   0       3
    #          /  \
    #         2    4
    root = RedBlackTreeNode(val = 5)
    x = RedBlackTreeNode(val=1)
    y = RedBlackTreeNode(val=3, color='red')
    root.left = x
    x.parent = root
    x.left = RedBlackTreeNode(val=0)
    x.left.left = RedBlackTreeNode()
    x.left.right = RedBlackTreeNode()
    x.right = y
    y.parent = x
    y.left = RedBlackTreeNode(val=2)
    y.left.left = RedBlackTreeNode()
    y.left.right = RedBlackTreeNode()
    y.right = RedBlackTreeNode(val=4)
    y.right.left = RedBlackTreeNode()
    y.right.right = RedBlackTreeNode()
    tree = RedBlackTree(root=root)
    return tree

def getTree4():
    # Tree4
    #           5
    #         /
    #        3
    #       /  \
    #     1     4
    #    / \
    #   0   2
    root = RedBlackTreeNode(val=5)
    x = RedBlackTreeNode(val=1,color='red')
    y = RedBlackTreeNode(val=3)
    root.left = y
    y.parent = root
    x.left = RedBlackTreeNode(val=0)
    x.right = RedBlackTreeNode(val=2)
    x.left.left = RedBlackTreeNode()
    x.left.right = RedBlackTreeNode()
    x.right.left = RedBlackTreeNode()
    x.right.right = RedBlackTreeNode()
    y.right = RedBlackTreeNode(val=4)
    y.right.left = RedBlackTreeNode()
    y.right.right = RedBlackTreeNode()
    y.left = x
    x.parent = y
    tree = RedBlackTree(root=root)
    return tree


def test_is_equal_tree():
    x = RedBlackTreeNode(val=1)
    y = RedBlackTreeNode(val=1)
    assert is_equal_tree(x,y)==True

def test_is_equal_tree_with_branch():
    x = RedBlackTreeNode(val=1)
    y = RedBlackTreeNode(val=3)
    x.left = RedBlackTreeNode(val=0)
    x.right = y
    y.parent = x
    y.left = RedBlackTreeNode(val=2)
    y.right = RedBlackTreeNode(val=4)
    assert is_equal_tree(x,y)==False

def test_is_equal_tree_nil():
    assert is_equal_tree(RedBlackTreeNode(),RedBlackTreeNode())

def test_left_rotate():
    tree1 = getTree1()
    tree2 = getTree2()
    tree1._left_rotate(tree1.root)
    assert is_equal_tree(tree1.root,tree2.root)

def test_left_rotate_not_from_root():
    tree3 = getTree3()
    tree4 = getTree4()
    tree3._left_rotate(tree3.root.left)
    assert is_equal_tree(tree3.root,tree4.root)

def test_right_rotate():
    tree1 = getTree1()
    tree2 = getTree2()
    tree2._right_rotate(tree2.root)
    assert is_equal_tree(tree1.root,tree2.root)

def test_right_rotate_not_from_root():
    tree3 = getTree3()
    tree4 = getTree4()
    tree4._right_rotate(tree4.root.left)
    assert is_equal_tree(tree3.root,tree4.root)

def test_is_redblacktree():
    tree = getTree3()
    assert is_redblacktree(tree)

def test_insert_black_parent():
    tree = getTree1()
    assert is_redblacktree(tree.insert(RedBlackTreeNode(val=1.5)))

def test_insert_red_parent():
    tree = getTree1()
    assert is_redblacktree(tree.insert(RedBlackTreeNode(val=0.5)))

def test_insert_red_parent():
    tree = getTree1()
    assert is_redblacktree(tree.insert(RedBlackTreeNode(val=-0.5)))