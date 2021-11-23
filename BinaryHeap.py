class Heap:
    def __init__(self,size) -> None:
        self.customList=(size+1)*[None]
        self.heapSize=0
        self.maxSize=size+1

def peekofHeap(rootNode):
    if not rootNode:
        return
    return rootNode.customList[1]

def sizeofHeap(rootNode):
    if not rootNode:
        return
    return rootNode.heapSize

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    for i in range(1,rootNode.heapSize+1):
        print(rootNode.customList[i])

#This function is to make sure the heap property is followed after insertion on available leaf node
#index is index of node to swap, heapType is min or max
def heapifyTreeInsert(rootNode,index,heapType):
    parentIndex=int(index/2)
    if index<=1:
        return
    if heapType=="min":
        if rootNode.customList[index]<rootNode.customList[parentIndex]:
            temp=rootNode.customList[index]
            rootNode.customList[index]=rootNode.customList[parentIndex]
            rootNode.customList[parentIndex]=temp
        heapifyTreeInsert(rootNode,parentIndex,heapType)

    elif heapType=="max":
        if rootNode.customList[index]>rootNode.customList[parentIndex]:
            temp=rootNode.customList[index]
            rootNode.customList[index]=rootNode.customList[parentIndex]
            rootNode.customList[parentIndex]=temp
        heapifyTreeInsert(rootNode,parentIndex,heapType)

def insertNode(rootNode,value,heapType):
    if rootNode.heapSize+1==rootNode.maxSize:
        return "Binary Heap is full"
    rootNode.customList[rootNode.heapSize+1]=value
    rootNode.heapSize+=1
    heapifyTreeInsert(rootNode,rootNode.heapSize,heapType)
    return "Value successfully inserted"

def heapifyTreeExtract(rootNode,index,heapType):
    leftIndex=index*2




bh=Heap(5)
insertNode(bh,4,"max")
insertNode(bh,5,"max")
insertNode(bh,2,"max")
insertNode(bh,1,"max")

levelOrderTraversal(bh)