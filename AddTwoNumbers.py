# Definition for singly-linked list.
# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry=0
        addedList=ListNode()
        dummy=addedList
        while l1 and l2:
            # print(l1,l2)
            value=l1.val+l2.val+carry
            # print(value)
            carry=int(value/10)
            l1=l1.next
            l2=l2.next
            newNode=ListNode()
            newNode.val=value%10
            dummy.next=newNode
            dummy=dummy.next
        if not(l1) and l2:
            while l2:
                newNode=ListNode()
                value=l2.val+carry
                carry=int(value/10)
                newNode.val=value%10
                dummy.next=newNode
                l2=l2.next
                dummy=dummy.next

        if l1 and not(l2):
            while l1:
                value=l1.val+carry
                carry=int(value/10)
                l1=l1.next
                newNode=ListNode(value%10)
                dummy.next=newNode
                dummy=dummy.next

        if carry!=0:
                newNode=ListNode(carry)
                dummy.next=newNode
                dummy=dummy.next

        return addedList.next

# Little consise
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry=0
        addedList=ListNode()
        dummy=addedList
        while l1 or l2:
            l1Val=l1.val if (l1!= None) else 0
            l2Val=l2.val if (l2!= None) else 0
            value=l1Val+l2Val+carry
            carry=int(value/10)
            if l1!=None:
                l1=l1.next
            if l2!=None:
                l2=l2.next
            newNode=ListNode(value%10)
            dummy.next=newNode
            dummy=dummy.next
        if carry!=0:
                newNode=ListNode(carry)
                dummy.next=newNode
                dummy=dummy.next
        return addedList.next
