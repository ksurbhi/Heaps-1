import heapq

class Solution:
    """
    Time Complexity: O(nlogk)
    Space Complexity: O(k)
    """
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Initialize an empty min-heap
        heap = []
        
        # Iterate through each number in the list
        for i in range(len(nums)):
            # Push the current number onto the heap
            heapq.heappush(heap, nums[i])
            
            # If the heap size exceeds k, remove the smallest element (to keep only k largest elements)
            if len(heap) > k:
                heapq.heappop(heap)
        
        # The root of the heap is the kth largest element
        return heap[0]

 

        
