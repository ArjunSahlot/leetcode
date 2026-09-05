# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from queue import PriorityQueue
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        q = PriorityQueue()
        for i in range(len(lists)):
            if lists[i] is not None:
                q.put((lists[i].val, i, lists[i]))
                lists[i] = lists[i].next
        
        head = ListNode()
        curr = head
        while not q.empty():
            n = q.get()
            curr.next = n[2]
            curr = curr.next
            if lists[n[1]] is not None:
                q.put((lists[n[1]].val, n[1], lists[n[1]]))
                lists[n[1]] = lists[n[1]].next
        
        return head.next