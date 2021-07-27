# Middle of the Linked List
# Given a non-empty, singly linked list with head node head, return a middle node of linked list.
# If there are two middle nodes, return the second middle node.

# Input: [1,2,3,4,5]
# Output: Node 3 from this list (Serialization: [3,4,5])
# The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
# Note that we returned a ListNode object ans, such that:
# ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#Naive Solution
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        count=0
        nextIter=head
        while nextIter!=None:
            count+=1
            nextIter=nextIter.next
        mid=int(count/2 if count%2==0 else (count/2)+1)
        while count!=mid:
            count-=1
            head=head.next
        return head

# Approach- Head moves slowly while fast moves twice the speed.
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        fast=head
        while fast and fast.next!=None:
            head=head.next
            fast=fast.next.next
        return head