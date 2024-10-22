/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    long long kthLargestLevelSum(TreeNode* root, int k) {
        priority_queue<long long> levels;

        vector<TreeNode*> curr = {root};
        while (!curr.empty()) {
            vector<TreeNode*> newcurr = {};
            long long sum = 0;
            for (TreeNode* node: curr) {
                sum += node->val;
                if (node->left != nullptr) newcurr.push_back(node->left);
                if (node->right != nullptr) newcurr.push_back(node->right);
            }
            levels.push(sum);
            curr = newcurr;
        }

        if (levels.size() < k) return -1;

        while (--k) {
            levels.pop();
        }
        return levels.top();
    }
};