class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def createLinkedList(arr):
    if not arr:
        return None
    head = Node(arr[0])
    current = head
    for val in arr[1:]:
        current.next = Node(val)
        current = current.next
    return head

def printLinkedList(head):
    arr = []
    current = head
    while current:
        arr.append(current.val)
        current = current.next
    print(arr)


def reverse(head):
    prev = None
    current = head
    
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    
    return prev  


l1 = [1,2,3,4,5]
l2 = [1,2]

head1 = createLinkedList(l1)
head2 = createLinkedList(l2)

a = reverse(head1)
b = reverse(head2)




head = createLinkedList([1, 2, 3, 4, 5])
print("Linked List:")
printLinkedList(head)
head = reverse(head)
print("Reversed Linked List:")
printLinkedList(head)


head = createLinkedList([1, 2])
print("Linked List:")
printLinkedList(head)
head = reverse(head)
print("Reversed Linked List:")
printLinkedList(head)


head = createLinkedList([])
print("Linked List:")
printLinkedList(head)
head = reverse(head)
print("Reversed Linked List:")
printLinkedList(head)

