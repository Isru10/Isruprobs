# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        count=0
        while temp:
            count+=1
            temp=temp.next
        temp=head
        i=0
        x=(count//2)
        if x==0:
            return None
        while temp:
            i+=1
            if (i!=x):
                temp=temp.next
            else:
                temp.next=temp.next.next
        return head