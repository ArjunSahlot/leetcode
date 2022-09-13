# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def getnum(node, num=0, unit=1, l=0):
            num += node.val*unit
            unit *= 10
            l += 1
            if node.next is not None:
                return getnum(node.next, num, unit)
            else:
                return num, l
        n1, l1 = getnum(l1)
        n2, l2 = getnum(l2)
        
        if l1 > l2:
            n2 = int("".join(map(str, reverse(([0]*(l1-l2)).extend(list(n2))))))
        elif l2 > l1:
            n1 = int("".join(map(str, reverse(([0]*(l2-l1)).extend(list(n1))))))

        total = str(n1 + n2)
        
        node = ListNode(int(total[0]), None)
        for i in total[1:]:
            node = ListNode(int(i), node)
        
        return node
        