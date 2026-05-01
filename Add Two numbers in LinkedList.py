# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=0
        dummy=ListNode(-1)
        curr=dummy
        t1=l1
        t2=l2
        node_sum=0
        while t1 or t2 or carry:
            node_sum=carry
            if t1:
                node_sum=node_sum+t1.val
                t1=t1.next
            if t2:
                node_sum=node_sum+t2.val
                t2=t2.next
            new_node=node_sum%10
            carry=node_sum//10
            curr.next=ListNode(new_node)
            curr=curr.next
        return dummy.next

# TC: O(MAX(m,n))
# SC : O(MAX(m,n)) 
