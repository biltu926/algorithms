'''You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.'''


# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        unit = 0
        tens = 0
        r = None
        value = 0

        while l1 != None and l2 != None:
            value = l1.val + l2.val
            if tens > 0:
                value += tens
                tens = 0
            if value >= 10:
                unit = value % 10
                tens = value // 10
                value = unit

            temp = ListNode(value)

            if r == None:
                r = temp
                h = r
            else:
                r.next = temp
                r = r.next
            l1 = l1.next
            l2 = l2.next

        while l1 != None:
            value = l1.val
            if tens > 0:
                value += tens
                tens = 0

            if value >= 10:
                unit = value % 10
                tens = value // 10
                value = unit

            temp = ListNode(value)
            if r == None:
                r = temp
                h = r
            else:
                r.next = temp
                r = r.next
            l1 = l1.next

        while l2 != None:
            value = l2.val
            if tens > 0:
                value += tens
                tens = 0

            if value >= 10:
                unit = value % 10
                tens = value // 10
                value = unit

            temp = ListNode(value)
            if r == None:
                r = temp
                h = r
            else:
                r.next = temp
                r = r.next
            l2 = l2.next

        if tens > 0:
            temp = ListNode(tens)
            r.next = temp
            r = r.next

        return h