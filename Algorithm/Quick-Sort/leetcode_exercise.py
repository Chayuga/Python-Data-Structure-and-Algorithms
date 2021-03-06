"""
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
"""

from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pivot = nums.pop()

        left = [x for x in nums if x < pivot]
        mid = [x for x in nums if x == pivot]
        right = [x for x in nums if x > pivot]

        L, M = len(left), len(mid)

        if k <= L:
            return self.findKthLargest(left, k)

        elif k > (L + M):
            return self.findKthLargest(right, k-(L+M))

        else:
            return mid[0]

    if __name__ == '__main__':
        sequence = [2, 6, 52, 1, 3, 0, 12]
        findKthLargest(List[sequence], k=2)

        print(sorted)
        

