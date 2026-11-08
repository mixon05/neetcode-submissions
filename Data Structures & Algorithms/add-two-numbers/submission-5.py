# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = ListNode((l1.val + l2.val) % 10)
        head = l3
        carry = (l1.val + l2.val) // 10
        l1 = l1.next
        l2 = l2.next                
        while l1 or l2:
            node_sum = 0
            if l1:
                node_sum += l1.val
            if l2:
                node_sum += l2.val
            val = (node_sum + carry) % 10
            carry = (node_sum + carry) // 10
            new_node = ListNode(val)
            l3.next = new_node
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            l3 = l3.next
        if carry:
            l3.next = ListNode(carry)
        return head
            
            
