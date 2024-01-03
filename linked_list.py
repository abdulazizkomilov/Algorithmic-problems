class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None
        

def print_element(head: Node) -> Node:
    curr = head
    while curr is not None:
        print(curr.val)
        curr = curr.next
    

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.next = node2
node2.next = node3
node3.next = node4

print_element(node1)
