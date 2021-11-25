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
    rightIndex=index*2+1
    swapChild=0
    # No children
    if rootNode.heapSize<leftIndex:
        return
    #Only one child
    if rootNode.heapSize==leftIndex:
        if heapType=="min":
            if rootNode.customList[index]>rootNode.customList[leftIndex]:
                temp=rootNode.customList[index]
                rootNode.customList[index]=rootNode.customList[leftIndex]
                rootNode.customList[leftIndex]=temp
            return
        else:
            if rootNode.customList[index]<rootNode.customList[leftIndex]:
                temp=rootNode.customList[index]
                rootNode.customList[index]=rootNode.customList[leftIndex]
                rootNode.customList[leftIndex]=temp
            return
    #Two children
    else:
        if heapType=="min":
            if rootNode.customList[leftIndex]<rootNode.customList[rightIndex]:
                swapChild=leftIndex
            else:
                swapChild=rightIndex
            if rootNode.customList[index]>rootNode.customList[swapChild]:
                temp=rootNode.customList[index]
                rootNode.customList[index]=rootNode.customList[swapChild]
                rootNode.customList[swapChild]=temp
        else:
            if rootNode.customList[leftIndex]>rootNode.customList[rightIndex]:
                swapChild=leftIndex
            else:
                swapChild=rightIndex
            if rootNode.customList[index]<rootNode.customList[swapChild]:
                temp=rootNode.customList[index]
                rootNode.customList[index]=rootNode.customList[swapChild]
                rootNode.customList[swapChild]=temp
        heapifyTreeExtract(rootNode,swapChild,heapType)

def extractNode(rootNode,heapType):
    if rootNode.heapSize==0:
        return
    extractedNode=rootNode.customList[1]
    rootNode.customList[1]=rootNode.customList[rootNode.heapSize]
    rootNode.customList[rootNode.heapSize]=None
    rootNode.heapSize-=1
    heapifyTreeExtract(rootNode,1,heapType)
    return extractedNode

def deleteEntireBH(rootNode):
    rootNode.customList=None


bh=Heap(5)
insertNode(bh,4,"max")
insertNode(bh,5,"max")
insertNode(bh,2,"max")
insertNode(bh,1,"max")

print(extractNode(bh,"max"))
print("Level order:")
levelOrderTraversal(bh)