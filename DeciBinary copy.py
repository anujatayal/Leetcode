
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def InsetNodeAtBegining(self, head: ListNode) -> ListNode:
        newHead=ListNode(val=10,next=head)
        return newHead
    def InsetNodeAtEnd(self, head: ListNode) -> ListNode:
        newHead=ListNode(val=10,next=None)
        if head ==None:
            return newHead
        prev=head
        while prev.next:
            prev=prev.next
        prev.next=newHead
        return head