class Solution:
    def pourWater(self, heights, V, K):
        """
        :type heights: List[int]
        :type V: int
        :type K: int
        :rtype: List[int]
        :Time complexity: O(V*N) where N == len(heights)
        """
        # NOTE: A faster solution with O(V + N)
        # https://leetcode.com/problems/pour-water/discuss/176259/O(V-+-n)-Solution-with-Two-Stacks
        graph = []
        for i, v in enumerate(heights):
            graph.append([])
            for _ in range(v):
                graph[i].append("#")

        # Main
        # Start from pour V volumn water
        for _ in range(V):
            index = K # by default, we assume it will fall to positon K
            
            for left in range(K - 1, -1, -1): # Try drop to [0:K]
                if heights[left] < heights[index]:
                    index = left # try to find the lowest part in [0:K]
                
                if heights[left] > heights[index]:
                    break
            
            if index == K: # We couldn't find an index in [0:K] lower then heights[K]
                for right in range(K + 1, len(heights)):
                    if heights[right] < heights[index]:
                        index = right
                        
                    if heights[right] > heights[index]:
                        break
                
            # NOTE: if we want to print water and container, do it here.
            graph[index].append('w')
            heights[index] += 1
        
        print("################")
        for line in graph:
            print "".join(line)
        print("################")
        return heights

obj = Solution()
heights = [2,1,1,2,1,2,2]
V = 4
K = 3
obj.pourWater(heights, V, K)          