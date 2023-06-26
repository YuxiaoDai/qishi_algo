# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()
        cur = dummy_head
        node_1 = list1
        node_2 = list2
        while node_1 or node_2:
            if not node_1:
                cur.next = node_2
                break
            if not node_2:
                cur.next = node_1
                break
            if node_1.val <= node_2.val:
                cur.next = ListNode(node_1.val)
                cur = cur.next
                node_1 = node_1.next
            else:
                cur.next = ListNode(node_2.val)
                cur = cur.next
                node_2 = node_2.next           
        
        return dummy_head.next