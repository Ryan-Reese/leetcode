# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # save first number into n
        n = 0
        exp = 0
        while True:
            n += (l1.val * 10**exp)
            l1 = l1.next
            exp += 1
            if (l1 == None):
                break
        # save second number into n
        exp = 0
        while True:
            n += (l2.val * 10**exp)
            l2 = l2.next
            exp += 1
            if (l2 == None):
                break
        # compute sum and save into return
        sum = ListNode()
        nxtptr = sum
        while (n//10 != 0):
            nxtptr.val = n%10
            nxtptr.next = ListNode()
            n = n//10
            nxtptr = nxtptr.next
        nxtptr.val = n%10
        return sum
