"""
    There are a row of n houses, each house can be painted with one of the k colors. 
    The cost of painting each house with a certain color is different. 
    You have to paint all the houses such that no two adjacent houses have the same color.

    The cost of painting each house with a certain color is represented by a n x k cost matrix. 
    For example, 
    costs[0][0] is the cost of painting house 0 with color 0; 
    costs[1][2] is the cost of painting house 1 with color 2, and so on... 
    Find the minimum cost to paint all houses.

    Note:
    All costs are positive integers.

    Example:
    Input: [[1,5,3],[2,9,4]]
    Output: 5
    Explanation: Paint house 0 into color 0, paint house 1 into color 2. Minimum cost: 1 + 4 = 5; 
                Or paint house 0 into color 2, paint house 1 into color 0. Minimum cost: 3 + 2 = 5. 
    Follow up:
    Could you solve it in O(nk) runtime?
"""
class Solution:
    def minCostII(self, costs):
        if not costs:
            return 0 #No house to paint
        if not costs[0]:
            return None #No color to paint
        
        dp=[[0]*len(costs[0]) for i in range(len(costs))]
        dp[0]=costs[0]
        
        def helper_min(A,i):
            res=A[0]
            resind=0
            for j in range(0,len(A)):
                if A[j]<res:
                    res=A[j]
                    resind=j
            B=[res+costs[i][j] for j in range(0,len(A))]
            B[resind]=costs[i][resind]+min(A[:resind]+A[resind+1:])
            return B       
        
        for i in range(1,len(costs)):
            dp[i]=helper_min(dp[i-1],i)
        
        
        return min(dp[-1])
        