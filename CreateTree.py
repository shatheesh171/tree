class TreeNode:
    def __init__(self,data,children=None) -> None:
        self.data=data
        if children is None:
            self.children=[]
        else:
            self.children=children
        
    def __str__(self,level=0) -> str:
        #return str(self.children)
        res=" "*level+str(self.data)+"\n"
        for child in self.children:
            res+=child.__str__(level+1)
        return res

    def addChild(self,treeNode):
        self.children.append(treeNode)


tree=TreeNode('Drinks')
cold=TreeNode('Cold')
hot=TreeNode('Hot')
tree.addChild(cold)
tree.addChild(hot)
print(tree)