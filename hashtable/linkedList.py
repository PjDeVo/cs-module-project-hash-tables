class Node:
    def __init__(self,value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        currStr = ""
        curr = self.head
        while curr != None:
            currStr = f'{str(curr.value())} ->'
            curr = curr.next
        return currStr

    def find(self,value):
        # return node w/value
        curr = self.head
        while curr != None:
            if curr.value == value:
                return curr
            curr = curr.next
        return None


    def delete(self,value):
        curr = self.head
        

        if curr.value == value:
            self.head = curr.next
            curr.next = None
            return curr

        prev = None

        while curr != None:
            if curr.value == value:
                prev.next = curr.next
                curr.next = None
            else:
                prev = curr
                curr = curr.next
        return None


    def insert_at_head(self,node):
        node.next = self.head
        self.head = node

    def insert_at_head_or_overwrite(self, node):
        existingNode = self.find(node.value)
        if existingNode != None:
            existingNode.value = node.value
        else:
            self.insert_at_head(node)