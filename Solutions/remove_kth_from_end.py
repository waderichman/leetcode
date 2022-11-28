class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fp, sp = head, head
        
        while n:
            sp = sp.next
            n -= 1
            
            
        if not sp:
            return head.next
        
        while sp.next:
            sp = sp.next
            fp = fp.next
        
        
        fp.next = fp.next.next
        return head
                

        