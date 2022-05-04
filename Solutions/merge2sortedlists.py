class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        if list1.val < list2.val:
            nexthead = self.mergeTwoLists(list1.next, list2)
            list1.next = nexthead
            return list1
        else:
            nexthead = self.mergeTwoLists(list2.next, list1)
            list2.next = nexthead
            return list2
