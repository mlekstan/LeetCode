#heap sort

from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        def cheap(parent_node_ptr, arr, length):
            left_node_ptr = 2 * parent_node_ptr + 1
            right_node_ptr = 2 * parent_node_ptr + 2
            largest_node_ptr = parent_node_ptr

            if left_node_ptr < length and arr[left_node_ptr] > arr[largest_node_ptr]:
                largest_node_ptr = left_node_ptr
            
            if right_node_ptr < length and arr[right_node_ptr] > arr[largest_node_ptr]:
                largest_node_ptr = right_node_ptr

            if largest_node_ptr != parent_node_ptr:
                arr[parent_node_ptr], arr[largest_node_ptr] = arr[largest_node_ptr], arr[parent_node_ptr]
                cheap(largest_node_ptr, arr, length)


        def heap_sort(arr):
            length = len(arr)
            for i in range((length-1)//2, -1, -1):
                cheap(i, arr, length)

            while length > 1: 
                arr[length-1], arr[0] = arr[0], arr[length-1]
                length -= 1
                cheap(0, arr, length)


        def compare(arr_1, arr_2):
            diff_count = 0
            for i in range(len(arr_1)):
                if arr_1[i] != arr_2[i]:
                    diff_count += 1
            
            return diff_count
        
        
        expected = heights[:]
        heap_sort(expected)

        return compare(heights, expected)
    


heights = [1,1,4,2,1,3]
print(Solution().heightChecker(heights))
