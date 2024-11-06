# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val= 0, next : Optional['ListNode']=None):

        self.val = val
        self.next = next

def reverseList(head : Optional[ListNode]):

    new_list_head = None
    while head != None:
        
        next_ = head.next
        if new_list_head != None:           

            head.next = new_list_head
            new_list_head = head

        else:
            new_list_head = head
            new_list_head.next = None
        head = next_
    return new_list_head

"""RECURSIVE CODE

def reverse(node: ListNode, reversed_list = None):
        
        if node == None:
            return reversed_list

        # recursive case
        next_ = node.next
        
        if reversed_list is None:
            reversed_list = node
            reversed_list.next = None
        
        else:
            node.next = reversed_list
            reversed_list = node

        return reverse(next_, reversed_list)

"""

