# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return None
            # is that just..none girl?
        fast=slow=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
            # now slow will become the middle value
            # it is this middle value where we will use to reorder the linked list and inject it back in ig

        curr=slow.next
        slow.next=None
        # these are all just aliases, we're really cutting off the linked list
        # so that we dont mess up our iteration
        # otherwise we'll have original+reversed and go into both while trying
        # to merge them, makes no sense right?
        prev=None
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp 
            # we keep the temp_next so that we know we're actually iterating through the list
            # been reversed
        
        # merge the 2 lists
        first=head
        second=prev # the middle, aka second half
        while second:
            temp1=first.next
            temp2=second.next
            first.next=second
            second.next=temp1
            # also simultaneously rearranging the linked list from the second half's POV
            first=temp1
            second=temp2
        # return head

        