import QueueLinkedList as queue

class TreeNode:
    def __init__(self,data) -> None:
        self.data=data
        self.leftChild=None
        self.rightChild=None

bt=TreeNode("Drinks")
leftChild=TreeNode("Hot")
rightChild=TreeNode("Cold")
tea=TreeNode("Tea")
coffee=TreeNode("Coffee")
leftChild.leftChild=tea
leftChild.rightChild=coffee
bt.leftChild=leftChild
bt.rightChild=rightChild

# Imagine what will happen at the leaf node (in which way it will print)
def preOrderTraversal(rootNode):    
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    cq=queue.Queue()
    cq.enqueue(rootNode)
    while not(cq.isEmpty()):
        root=cq.dequeue()
        print(root.value.data)
        if root.value.leftChild is not None:
            cq.enqueue(root.value.leftChild)
        if root.value.rightChild is not None:
            cq.enqueue(root.value.rightChild)


def searchBT(rootNode, value):
    if not rootNode:
        return "Tree does not exist"
    cq=queue.Queue()
    cq.enqueue(rootNode)
    while not(cq.isEmpty()):
        root=cq.dequeue()
        if root.value.data==value:
            return "Success"
        if root.value.leftChild is not None:
            cq.enqueue(root.value.leftChild)
        if root.value.rightChild is not None:
            cq.enqueue(root.value.rightChild)
    return "Not Found"
    
def insertNodeBT(rootNode,newNode):
    if not rootNode:
        rootNode=newNode
        return rootNode
    cq=queue.Queue()
    cq.enqueue(rootNode)
    while not(cq.isEmpty()):
        root=cq.dequeue()
        if root.value.leftChild is not None:
            cq.enqueue(root.value.leftChild)
        else:
            root.value.leftChild=newNode
            return "Inserted successfully"
        if root.value.rightChild is not None:
            cq.enqueue(root.value.rightChild)
        else:
            root.value.leftChild=newNode
            return "Inserted successfully"

# For deletion, get the deepest node in B tree, and replace it in place where node is to be deleted.
def getDeepestNode(rootNode):
    if not rootNode:
        return
    cq=queue.Queue()
    cq.enqueue(rootNode)
    while not(cq.isEmpty()):
        root=cq.dequeue()
        if root.value.leftChild is not None:
            cq.enqueue(root.value.leftChild)
        if root.value.rightChild is not None:
            cq.enqueue(root.value.rightChild)
    deepestNode=root.value
    return deepestNode


def deleteDeepestNode(rootNode,dNode):
    if not rootNode:
        return
    cq=queue.Queue()
    cq.enqueue(rootNode)
    while not(cq.isEmpty()):
        root=cq.dequeue()
        if root.value is dNode:
            root.value=None
            return
        if root.value.rightChild:
            if root.value.rightChild is dNode:
                root.value.rightChild=None
                return
            else:
                cq.enqueue(root.value.rightChild)

        if root.value.leftChild:
            if root.value.leftChild is dNode:
                root.value.leftChild=None
                return
            else:
                cq.enqueue(root.value.leftChild)
    

def deleteNodeBT(rootNode,node):
    if not rootNode:
        return "BT does not exist"
    cq=queue.Queue()
    cq.enqueue(rootNode)
    while not(cq.isEmpty()):
        root=cq.dequeue()
        if root.value.data==node:
            dNode=getDeepestNode(rootNode)
            root.value.data=dNode.data
            deleteDeepestNode(rootNode,dNode)
            return "Root has been successfully deleted"

        if root.value.leftChild is not None:
            cq.enqueue(root.value.leftChild)
        if root.value.rightChild is not None:
            cq.enqueue(root.value.rightChild)

    return "Failed to delete"

def deleteBT(rootNode):
    rootNode.data=None
    rootNode.leftChild=None
    rootNode.rightChild=None
    return "Binary Tree has been successfully deleted"



print(searchBT(bt,"Tea"))

cola=TreeNode("Cola")
insertNodeBT(bt,cola)

# dNode=getDeepestNode(bt)
# deleteDeepestNode(bt,dNode)

deleteNodeBT(bt,'Tea')

levelOrderTraversal(bt)