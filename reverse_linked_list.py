class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None
        

def reverseList(head):
    prev = None
    curr = head

    while curr is not None:
        next_ = curr.next
        curr.next = prev
        prev = curr
        curr = next_
    return prev

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.next = node2
node2.next = node3
node3.next = node4

print(reverseList(node1))
print(node4.next.val)