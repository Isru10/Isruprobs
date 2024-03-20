# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        tort=hare=list1
        pointer=lastn=list2
        while a >1:
            tort=tort.next
            a-=1
        while b >0:
            hare=hare.next 
            b-=1
        l=0
        while pointer:
            pointer=pointer.next 
            l+=1
        for i in range(l-1):
            lastn=lastn.next 
        tort.next =list2
        lastn.next =hare.next 
        return list1