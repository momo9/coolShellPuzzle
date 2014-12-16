#!/usr/bin/python

IN_ORDER = 'T, b, H, V, h, 3, o, g, P, W, F, L, u, A, f, G, r, m, 1, x, J, 7, w, e, 0, i, Q, Y, n, Z, 8, K, v, q, k, 9, y, 5, C, N, B, D, 2, 4, U, l, c, p, I, E, M, a, j, 6, S, R, O, X, s, d, z, t'
POST_ORDER = 'T, V, H, o, 3, h, P, g, b, F, f, A, u, m, r, 7, J, x, e, w, 1, Y, Q, i, 0, Z, n, G, L, K, y, 9, k, q, v, N, D, B, C, 5, 4, c, l, U, 2, 8, E, I, R, S, 6, j, d, s, X, O, a, M, p, W, t, z'

class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


def trav(treeNode):
    print treeNode.val, '#' if treeNode.left == None else treeNode.left.val, '#' if treeNode.right == None else treeNode.right.val
    if treeNode.left != None:
        trav(treeNode.left)
    if treeNode.right != None:
        trav(treeNode.right)


def allPath(treeNode, s):
    cur = s + treeNode.val
    print cur
    if treeNode.left != None:
        allPath(treeNode.left, cur)
    if treeNode.right != None:
        allPath(treeNode.right, cur)


def strToList(s):
    return [x.strip() for x in s.split(',')]


def getTree(inOrder, postOrder):
    node = TreeNode(postOrder[-1], None, None)
    pivot = inOrder.index(node.val)
    if pivot != 0:
        node.left = getTree(inOrder[0 : pivot], postOrder[0 : pivot])
    else:
        node.left = None
    if pivot != len(inOrder) - 1:
        node.right = getTree(inOrder[pivot + 1:], postOrder[pivot : -1])
    else:
        node.right = None
    return node


if __name__ == "__main__":
    inOrder = strToList(IN_ORDER)
    postOrder = strToList(POST_ORDER)
    treeNode = getTree(inOrder, postOrder)
    allPath(treeNode, '')
