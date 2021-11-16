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

levelOrderTraversal(bt)