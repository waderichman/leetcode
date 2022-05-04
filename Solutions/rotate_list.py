class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        
        last = head
        length = 1
        while last.next:
            length+=1
            last = last.next
        last.next = head
        curr = head
        
        
        for i in range(length-(k%length)-1):
            curr = curr.next
        res = curr.next
        curr.next = None
        
        return res
            