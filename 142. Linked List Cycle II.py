class Solution(object):
    def detectCycle(self, head):
    
        if head is None or head.next is None:
            return None
        slow = head
        fast = head

        found = False
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                found = True
                break

        if not found:
            return None

        start = head
        while start != slow:
            start = start.next
            slow = slow.next

        return start