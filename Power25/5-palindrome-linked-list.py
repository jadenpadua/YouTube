# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        # Step 1: find the middle
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        # Step 2: reverse LL 
        prev = None
        while slow:
            temp = slow
            slow = slow.next
            temp.next = prev
            prev = temp
            
        # Step 3: Compare first and second half
        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
            
        return True
