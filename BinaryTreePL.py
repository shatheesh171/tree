# Binary Tree implemented using python list

class BinaryTree:
    def __init__(self,size) -> None:
        self.cl=size*[None]
        self.lastUsedIndex=0
        self.maxSize=size

    def insertNode(self,value):
        if self.lastUsedIndex+1==self.maxSize:
            return "BT is full"
        self.cl[self.lastUsedIndex+1]=value
        self.lastUsedIndex+=1
        return "value successfully inserted"

    def searchNode(self,value):
        if value in self.cl:
            return "Success"
        return "Failed"

    def preOrderTraversal(self,index=1):
        if index>self.lastUsedIndex:
            return
        print(self.cl[index])
        #call left subtree
        self.preOrderTraversal(index*2)
        self.preOrderTraversal(index*2+1)

    def inOrderTraversal(self,index=1):
        if index>self.lastUsedIndex:
            return
        self.inOrderTraversal(index*2)
        print(self.cl[index])
        self.inOrderTraversal(index*2+1)

    def postOrderTraversal(self,index=1):
        if index>self.lastUsedIndex:
            return
        self.postOrderTraversal(index*2)
        self.postOrderTraversal(index*2+1)
        print(self.cl[index])

    def levelOrderTraversal(self,index=1):
        for i in range(index,self.lastUsedIndex+1):
            print(self.cl[i])


    def deleteNode(self,value):
        if self.lastUsedIndex==0:
            return "List is empty"

        for i in range(1,self.lastUsedIndex+1):
            if self.cl[i]==value:
                self.cl[i]=self.cl[self.lastUsedIndex]
                self.cl[self.lastUsedIndex]=None
                self.lastUsedIndex-=1
                return "Node successfully deleted"

    def deleteBT(self):
        self.cl=None
        return "BT deleted successfully"



bt=BinaryTree(8)
bt.insertNode("drinks")
bt.insertNode("hot")
bt.insertNode("cold")
bt.insertNode("tea")
bt.insertNode("coffee")
print(bt.searchNode('hot'))

print(bt.deleteNode('tea'))
#bt.preOrderTraversal()
#bt.inOrderTraversal()
#bt.postOrderTraversal()
bt.levelOrderTraversal()