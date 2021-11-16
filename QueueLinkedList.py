class Node:
    def __init__(self,value) -> None:
        self.value=value
        self.next=None

    def __str__(self) -> str:
        return str(self.value)

class LinkedList:
    def __init__(self) -> None:
        self.head=None
        self.tail=None

    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next

class Queue:
    def __init__(self) -> None:
        self.ll=LinkedList()

    def __str__(self) -> str:
        values=[str(x.value) for x in self.ll]
        return ' '.join(values)

    def enqueue(self,value):
        node=Node(value)
        if self.ll.head is None:
            self.ll.head=node
            self.ll.tail=node
        else:
            self.ll.tail.next=node
            self.ll.tail=node

    def isEmpty(self):
        if self.ll.head is None:
            return True
        return False

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"        
        node=self.ll.head
        if self.ll.head==self.ll.tail:
            self.ll.head=None
            self.ll.tail=None
            return node
        self.ll.head=self.ll.head.next
        return node

    def peek(self):
        if self.isEmpty():
            return "Queue is empty"        
        return self.ll.head
    
    def delete(self):
        self.ll.head=None
        self.ll.tail=None


