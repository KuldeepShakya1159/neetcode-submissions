# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        dummy = ListNode()

        for i in range(len(lists)-1):
            lists[i+1] = self.mergelist(lists[i],lists[i+1])
            dummy.next = lists[i+1]
        return dummy.next

    
    def mergelist(self,list1,list2):

        dummy = ListNode()
        node = dummy

        while list1 and list2:
            if list1.val>list2.val:
                dummy.next = list2
                list2=list2.next
            else:
                dummy.next = list1
                list1 = list1.next
            dummy = dummy.next
        dummy.next = list1 or list2

        return node.next
            

        