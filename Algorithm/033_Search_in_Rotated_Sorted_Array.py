# No duplicated numbers
class Solution:
    def search_easy_understand(self, nums: List[int], target: int) -> int:
        #Runtime: 44 ms, faster than 94.58% of Python3 online submissions for Search in Rotated Sorted Array.
        # Memory Usage: 14.2 MB, less than 6.29% of Python3 online submissions for Search in Rotated Sorted Array.
        if not nums:
            return -1
        
        left = 0
        right = len(nums) - 1
        
        # No overlapping
        while left < right:
            mid = left + (right - left) // 2
            if target == nums[mid]:
                return mid
            
            if nums[mid] < nums[left]:
                # Right side in order
                # Largest on the left
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid
            else:
                # nums[mid] >= nums[left]
                # left side in order
                # Largest == mid or Largest on the right
                if target >= nums[left] and target < nums[mid]:
                    right = mid
                else:
                    left = mid + 1
                    
        return left if nums[left] == target else -1

    def search_no_edge_case(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        # pointer could be overlapping. 
        while left <= right:
            mid = left + (right - left) // 2
            if target == nums[mid]:
                return mid
            
            # Note: here left is the pivot, we cover all cases by letting
            # nums[mid] could == nums[left]
            if nums[mid] >= nums[left]:
                # left half in order
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] < nums[right]:
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1