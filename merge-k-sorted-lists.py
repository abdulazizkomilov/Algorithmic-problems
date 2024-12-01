class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for value in lst[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
linked_lists = [create_linked_list(lst) for lst in lists]

def create_linked_lists(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for value in lst[1:]:
        current.next = ListNode(value)
        current = current.next
    return head
        
def mergeKLists(lists) -> ListNode:
    nums = []
    
    for lst in lists:
        head = lst
        while head:
            nums.append(head.val)
            head = head.next
    
    head = create_linked_list(sorted(nums))
    return head

print(mergeKLists(linked_lists))
