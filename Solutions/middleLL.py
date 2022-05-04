class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        len = 0
        pt1, pt2 = head, head
        while pt1:
            len +=1
            pt1 = pt1.next
        middle = len // 2
        count = 0
        while pt2:
            if count == middle:
                return pt2
            else:
                count +=1
                pt2 = pt2.next
        return None