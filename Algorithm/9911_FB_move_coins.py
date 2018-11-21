"""
    Given a tree with n nodes. Each node has k coins, where 0 <= k <= n . 
    There are total n coins on the tree. 
    The goal is to move the coins such that each node has exactly one coin. 
    What's the minimum moves required? 

    int moveCoins(TreeNode root) {
        return dfs(root, new HashMap<>());
    }

    int dfs(TreeNode n, Map<TreeNode, Integer> count) {
        if(!count.containsKey(n)) {
            count.put(n, n.val);
        }
        int coinsNum = count.get(n);
        int res = 0;
        for(TreeNode kid : n.children) {
            res += dfs(kid, count);
            coinsNum += count.get(kid);
            res += Math.abs(count.get(kid));
        }
        count.put(n, coinsNum - 1);
        return res;
    }
"""
