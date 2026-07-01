# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        elif not list1 and list2:
            return list2
        elif not list2 and list1:
            return list1

        res = curr = ListNode

        while list1 and list2:
            
            # prev=curr
            if list2.val<list1.val:
                    # prev=list2
                curr.next=list2
                list2=list2.next
            else:
                curr.next=list1
                list1=list1.next
            curr=curr.next
            # dont forget to iterate through the sorted merged list we're creating!!!
        if not list1:
            curr.next=list2
        if not list2:
            curr.next=list1

        return res.next
