# Binary search tree using linked list
from BinaryTree import searchBT
import QueueLinkedList as queue

class BSTNode:
    def __init__(self,data) -> None:
        self.data=data
        self.leftChild=None
        self.rightChild=None

def insertNode(rootNode,value):
    if rootNode.data is None:
        rootNode.data=value
        return "Successfully inserted"
    
    if value<=rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild=BSTNode(value)
        else:
            insertNode(rootNode.leftChild,value)
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild=BSTNode(value)
        else:
            insertNode(rootNode.rightChild,value)

    return "Node successfully inserted"

def preOrderTraversal(rootNode):
    if rootNode is None:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

def inOrderTraversal(rootNode):
    if rootNode is None:
        return    
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode):
    if rootNode is None:
        return    
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)
    
def levelOrderTraversal(rootNode):
    if rootNode is None:
        return    
    cq=queue.Queue()
    cq.enqueue(rootNode)
    while not cq.isEmpty():
        root = cq.dequeue()
        print(root.value.data)
        if root.value.leftChild:
            cq.enqueue(root.value.leftChild)
        if root.value.rightChild:
            cq.enqueue(root.value.rightChild)

def searchNode(rootNode,value):
    if rootNode is None:
        print("value not found")
        return
    if rootNode.data==value:
        print("Value is found")
        return
    if value<rootNode.data:
        searchNode(rootNode.leftChild,value)
    else:
        searchNode(rootNode.rightChild,value)
    #print("Value is not found")

#Deletion of node
#to replace deleted node (if 2 children), replace with min node in right subtree
def minValueNode(bstNode):
    current=bstNode
    while current.leftChild:
        current=current.leftChild
    return current


def deleteNode(rootNode,value):
    if rootNode is None:
        return rootNode
    # Here the rootnode is traversed according to conditions and returned value is updated 
    # accordingly on left and right child. It also works when value is not found
    if value<rootNode.data:
        rootNode.leftChild=deleteNode(rootNode.leftChild,value)
    elif value>rootNode.data: 
        rootNode.rightChild=deleteNode(rootNode.rightChild,value)
    else:
        #Value matches
        #One child
        if rootNode.leftChild is None:
            temp=rootNode.rightChild
            rootNode=None
            return temp

        if rootNode.rightChild is None:
            temp=rootNode.leftChild
            rootNode=None
            return temp

        #2 children
        temp=minValueNode(rootNode.rightChild)
        rootNode.data=temp.data
        #Now delete the temp node
        rootNode.rightChild=deleteNode(rootNode.rightChild,temp.data)
    return rootNode

def deleteBST(rootNode):
    rootNode.data=None
    rootNode.leftChild=None
    rootNode.rightChild=None
    return "BST successfully deleted"

bst=BSTNode(30)
print(insertNode(bst,25))
print(insertNode(bst,12))
print(insertNode(bst,34))
print(insertNode(bst,65))
print(insertNode(bst,32))
deleteNode(bst,30)
levelOrderTraversal(bst)
searchNode(bst,54)