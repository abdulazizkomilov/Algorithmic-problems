def middleNode(head):
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    return slow



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        

def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head



def print_linked_list(head):
    current = head
    result = []
    while current:
        result.append(current.val)
        current = current.next
    print(result)



head1 = create_linked_list([1, 2, 3, 4, 5])
middle1 = middleNode(head1)
print(middle1.val)

# print_linked_list(middle1)

head2 = create_linked_list([1, 2, 3, 4, 5, 6])
middle2 = middleNode(head2)
print(middle2.val)

# print_linked_list(middle2)



