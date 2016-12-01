#include <iostream>
 
class BinTreeNode(object):
 
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None


def tree_insert( tree, item):
    if tree==None:				    ##if the tree is empty
        tree=BinTreeNode(item)                      ## adds the first value to the root node
    elif(item < tree.value):
        if(tree.left==None):
            tree.left=BinTreeNode(item)         ## a node is added with the item if the left side of the tree not empty
        else:
            tree_insert(tree.left,item)         ## goes down the left side of the tree
    else:
        if(tree.right==None):
            tree.right=BinTreeNode(item)        ##inserts node with value at right side of the tree/branch
        else:
            tree_insert(tree.right,item)        ## goes down the right side of the tree
    return tree
 
def postorder(tree):
    if(tree.left!=None):
        postorder(tree.left)
    if(tree.right!=None):
        postorder(tree.right)
    print (tree.value)
 

def in_order(tree):
    currentNode = tree
    stack = []

    while currentNode:
        print( currentNode.value )
        
        if currentNode.left != None:
            stack.append(currentNode.value)

            currentNode = currentNode.left
        elif currentNode.right != None:
            stack.append(currentNode.value)
        if currentNode.right != None:
            stack.pop()
            
        if stack == []:
            print("break")
            break

if __name__ == '__main__':
   
    t=tree_insert(None,6);
    tree_insert(t,10)
    tree_insert(t,5)
    tree_insert(t,2)
    tree_insert(t,3)
    tree_insert(t,4)
    tree_insert(t,11)
    in_order(t)
