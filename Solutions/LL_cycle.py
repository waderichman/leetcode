class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        pt1 = head
        pt2 = head
    
        while pt2 != None and pt2.next != None:
            pt1 = pt1.next
            pt2 = pt2.next.next
            if pt1 == pt2:
                return True
        return False