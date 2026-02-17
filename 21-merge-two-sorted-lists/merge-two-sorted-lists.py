#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 1. Create a "Dummy" node
            dummy=ListNode(0)
            # 2. Create a "Tail" pointer that starts at the dummy
            tail=dummy
            # 3. While both lists still have nodes to compare
            while list1 and list2:
                # Compare the values at the current heads of both lists
                if list1.val<=list2.val:
                # If list1's value is smaller, connect our tail to list1
                    tail.next=list1
                # Move the list1 pointer forward to the next node
                    list1 = list1.next
                else:
                    # If list2's value is smaller, connect our tail to list2
                    tail.next=list2
                    # Move the list2 pointer forward
                    list2=list2.next

                # Move our tail pointer forward to the node we just added
                tail=tail.next

                # 4. Attach the "leftovers"
        # If one list is finished, just point the tail to the rest of the other list
            if list1:
                tail.next=list1
            elif list2:
                tail.next = list2

                # 5. Return the head of the new list
        # We return dummy.next because dummy itself was just a placeholder
            return dummy.next
        

        