class TrieNode:
    def __init__(self) -> None:
        self.children={}
        self.endOfString=False

class Trie:
    def __init__(self) -> None:
        self.root=TrieNode()

    def insertString(self,word):
        current=self.root
        # Loop and check if character exists in trie
        for i in word:
            ch=i
            # Check if character exists by dictionary key get method
            node=current.children.get(ch)
            if node is None:
                node=TrieNode()
                current.children.update({ch:node})
            current=node
        current.endOfString=True
        print("Successfully inserted")

    def searchString(self,word):
        current=self.root
        for i in word:
            node=current.children.get(i)
            if node is None:
                return False
            current=node
        if current.endOfString==True:
            return True
        return False

def deleteString(root,word,index):
    ch=word[index]
    current=root.children.get(ch)
    canDelete=False
    
    #At the last node
    if index==len(word)-1:
        if len(current.children)>=1:
            current.endOfString=False
            return False
        else:
            root.children.pop(ch)
            return True

    # if node's children more than 1, then we can't del the node
    if len(current.children)>1:
        # print("more than 1 child: "+ch)
        deleteString(current,word,index+1)
        return False

    #This is used in case of backtracking, if we are not at last index and get endOfString
    # we cannot delete from here eg (APIS,AP) delete APIS
    if current.endOfString==True:
        deleteString(current,word,index+1)
        return False

    canDelete=deleteString(current,word,index+1)
    if canDelete==True:
        root.children.pop(ch)
        return True
    return False



trie=Trie()
trie.insertString("App")
# trie.insertString("Appl")
# #trie.insertString("Appr")
# trie.insertString("AB")
# trie.insertString("Apr")
print(trie.root.children)
print(deleteString(trie.root,"App",0))
print(trie.searchString("App"))
print(trie.root.children)