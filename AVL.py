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



avl=AVLNode(10)
levelOrderTraversal(avl)