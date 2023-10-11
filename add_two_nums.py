# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807

# Input: l1 = [0], l2 = [0]
# Output: [0]


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addtwonumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = cur = ListNode()
        carryover = 0
        
        while l1 or l2:
            d = carryover
            if l1 and l2:
                d += (l1.val + l2.val)
                l1 = l1.next; l2 = l2.next
            elif l1:
                d += l1.val
                l1 = l1.next
            elif l2:
                d += l2.val
                l2 = l2.next
            carryover = d // 10
            cur.next = ListNode(d%10)
            cur = cur.next
        
        if carryover == 1: 
            cur.next = ListNode(1)
        return head.next



l_1 = [2, 4, 3]
l_2 = [5, 6, 4]
res = [7, 0, 8]

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)


solution = Solution()


result = solution.addtwonumbers(l1, l2)

while result:
    print(result.val)
    result = result.next