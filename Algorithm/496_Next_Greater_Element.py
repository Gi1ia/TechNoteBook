class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        greater = collections.defaultdict(int)
        stack = []
        
        for num in nums2:
            while stack and stack[-1] < num:
                greater[stack.pop()] = num
            stack.append(num)
        
        for i in range(len(stack)):
            greater[stack[i]] = -1
        
        res = []
        for i in range(len(nums1)):
            res.append(greater[nums1[i]])
        
        return res