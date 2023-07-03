# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge2Lists(self, list1, list2):
        dummy_head = ListNode()
        cur = dummy_head

        while list1 or list2:

            if not list1:
                cur.next = list2
                break
            if not list2:
                cur.next = list1
                break

            if list1.val > list2.val:
                cur.next = ListNode(val = list2.val)
                cur = cur.next
                list2 = list2.next
            else:
                cur.next = ListNode(val = list1.val)
                cur = cur.next
                list1 = list1.next
        
        return dummy_head.next

    def merge(self,lists, left, right):
        if left == right:
            return lists[left]
        mid = left + (right - left) // 2
        print(f'left is {left}')
        print(f'right is {right}')
        print(f'mid is {mid}')

        l1 = self.merge(lists, left, mid)
        l2 = self.merge(lists, mid+1, right)
        
        result = self.merge2Lists(l1, l2)
        print(f'left is [{left}:{mid}]')
        print(f'right is [{mid+1}:{right}]')
        print(result)

        return result

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:return 
        n = len(lists)
        return self.merge(lists, 0, n-1)


