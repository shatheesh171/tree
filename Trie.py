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


trie=Trie()
trie.insertString("App")
trie.insertString("Appl")
trie.insertString("B")
print(trie.root.children)
print(trie.searchString("App"))