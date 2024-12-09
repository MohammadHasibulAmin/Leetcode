#https://leetcode.com/problems/reverse-linked-list/

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = None
        temp = head

        while temp:
            n = temp.next
            temp.next = new_head
            new_head = temp
            temp = n
            
        return new_head