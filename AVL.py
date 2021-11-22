import QueueLinkedList as queue

class AVLNode:
    def __init__(self,data) -> None:
        self.data=data
        self.leftChild=None
        self.rightChild=None
        self.height=1

def preOrderTraversal(rootNode):
    if not rootNode:
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
    if rootNode.data==value:
        print("Node is found")
        return
    if value<rootNode.data:
        if rootNode.leftChild.data==value:
            print("Node is found")
            return
        searchNode(rootNode.leftChild,value)
    else:
        if rootNode.rightChild.data==value:
            print("Node is found")
            return
        searchNode(rootNode.rightChild,value)

def getHeight(rootNode):
    if not rootNode:
        return 0
    return rootNode.height


def rightRotate(disbalancedNode):
    newRoot=disbalancedNode.leftChild
    disbalancedNode.leftChild=disbalancedNode.leftChild.rightChild
    newRoot.rightChild=disbalancedNode
    disbalancedNode.height=1+max(getHeight(disbalancedNode.leftChild),getHeight(disbalancedNode.rightChild))
    newRoot.height=1+max(getHeight(newRoot.leftChild),getHeight(newRoot.rightChild))
    return newRoot

def leftRotate(disbalancedNode):
    newRoot=disbalancedNode.rightChild
    disbalancedNode.rightChild=disbalancedNode.rightChild.leftChild
    newRoot.leftChild=disbalancedNode
    disbalancedNode.height=1+max(getHeight(disbalancedNode.leftChild),getHeight(disbalancedNode.rightChild))
    newRoot.height=1+max(getHeight(newRoot.leftChild),getHeight(newRoot.rightChild))
    return newRoot

def getBalance(rootNode):
    if not rootNode:
        return 0
    return getHeight(rootNode.leftChild)-getHeight(rootNode.rightChild)

def insertNode(rootNode,value):
    if not rootNode:
        return AVLNode(value)
    if value<rootNode.data:
        rootNode.leftChild=insertNode(rootNode.leftChild,value)
    else:
        rootNode.rightChild=insertNode(rootNode.rightChild,value)

    rootNode.height=1+max(getHeight(rootNode.leftChild),getHeight(rootNode.rightChild))

    balance=getBalance(rootNode)

    if balance>1 and value<rootNode.leftChild.data:
        return rightRotate(rootNode)
    if balance>1 and value>rootNode.leftChild.data:
        rootNode.leftChild=leftRotate(rootNode.leftChild)
        return rightRotate(rootNode)
    if balance<-1 and value>rootNode.rightChild.data:
        return leftRotate(rootNode)
    if balance<-1 and value<rootNode.rightChild.data:
        rootNode.rightChild=rightRotate(rootNode.rightChild)
        return leftRotate(rootNode)

    return rootNode


avl=AVLNode(5)
avl=insertNode(avl,10)
avl=insertNode(avl,15)
avl=insertNode(avl,20)


levelOrderTraversal(avl)