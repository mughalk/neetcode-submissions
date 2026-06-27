# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head_val=head
        prev=None
        curr=head

        if not head or head.val==None:
            return None
        while curr:
            temp=curr.next
            # temp=1
            curr.next=prev
            # curr.next=None
            # switch the values
            # so 0,1,2,3
            # 1,0
            # then 2,1,0
            prev=curr
            # prev=0
            curr=temp
            # curr=1
        # tail=curr
        # head_val.next=
        return prev