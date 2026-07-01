# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # store a number and check if it points back to a previous number
        fast=head
        slow=head
        # find the tail
        hash_set=set()
        while slow:
            if slow in hash_set:
                # we actually can create a hash set because these are all unique objects
                return True
            hash_set.add(slow)
            slow=slow.next
        return False
        # while fast and fast.next:
        #     if fast.next==None:
        #         return False
        #     if fast==slow:
        #         return True
        #         # theyre pointing to the same
        #     fast=fast.next.next
        #     slow=slow.next
        
        # return False
