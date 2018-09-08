#96. Unique Binary Search Trees


'''
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''



class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """

        dp = [0]*(n + 1)
        dp[0] = 1
        
        for i in range(1, n + 1):
            for j in range(i):
                dp[i] += dp[j]*dp[i - j -1]
        return dp[n]

        # dp, Time complexity: O(n^2), space complexity: O(n)


'''
Denote by F(n) the number of unique BSTs containing 1,...,n. Now we can pick root.val be to any of the n values. 
Say we pick root.val = i, then the left subtree contains 1,...,i-1, and the right subtree contains i+1,...,n. 
The number of possible left subtrees is then F(i-1), and the number of possible right subtrees is F(n-i). 
The total number of BSTs with root.val = i is then F(i-1)*F(n-i). The total number of BSTs is then obtained 
by summing over i = 0,1,...,n-1 the expression F(i-1)*F(n-i). A naive recursive algorithm solving the recursion relation is:
'''
# recursion
def numTrees(self, n):
    """
    :type n: int
    :rtype: int
    """
    if n == 0:
        return 1
    elif n == 1:
        return 1
    res = 0
    for i in range(n):
        res += self.numTrees(i)*self.numTrees(n-1-i)
    return res
    # Time limit exceeded