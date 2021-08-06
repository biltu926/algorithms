# Leetcode problem link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        curr_node = head
        curr_pos = 0

        def mark_node(curr, n):
            if not curr.next:
                curr_pos = 2
                if n == 1:
                    return (curr_pos, False)
                return (curr_pos, True)

            curr_pos, flag = mark_node(curr.next, n)

            if curr_pos == n:
                return curr_pos + 1, False

            if not flag:
                curr.next = curr.next.next

            return curr_pos + 1, True

        _, flag = mark_node(curr_node, n)
        if not flag:
            head = head.next

        return head