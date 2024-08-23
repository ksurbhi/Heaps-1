# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:
    '''
    Time Complexity: O(NK logK)
    Space Complexity: O(K)
    '''
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        heap = []  # Min-heap to store the nodes based on their values

        # Create a dummy node to help build the final merged list
        dummy = ListNode(-1)

        # Push the head of each linked list into the heap
        for l in lists:
            print(l)
            if l:  # Ensure the linked list is not empty
                heapq.heappush(heap, (l.val, l))  # Push tuple of (value, node) into the heap

        # Pointer to track the end of the merged list
        curr = dummy

        # While there are elements in the heap
        while len(heap) > 0:
            # Pop the smallest element (node) from the heap
            val, Min = heapq.heappop(heap)

            # Attach the smallest node to the current end of the merged list
            curr.next = Min

            # Move the current pointer to the new end of the merged list
            curr = curr.next

            # If the extracted node has a next node, push it into the heap
            if Min.next is not None:
                heapq.heappush(heap, (Min.next.val, Min.next))

        # Return the merged list (dummy.next skips the initial dummy node)
        return dummy.next
