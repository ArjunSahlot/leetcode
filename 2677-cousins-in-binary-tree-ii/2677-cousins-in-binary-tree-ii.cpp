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
    TreeNode* replaceValueInTree(TreeNode* root) {
        int cursum = root->val;
        vector<vector<TreeNode*>> level = {{root}};
        while (!level.empty()) {
            for (vector<TreeNode*> sibs: level) {
                int sibsum = 0;
                for (TreeNode* node: sibs) {
                    sibsum += node->val;
                }
                for (TreeNode* node: sibs) {
                    node->val = cursum - sibsum;
                }
            }

            cursum = 0;
            vector<vector<TreeNode*>> newlevel;
            for (vector<TreeNode*> sibs: level) {
                for (TreeNode* node: sibs) {
                    vector<TreeNode*> futuresibs;
                    if (node->left != nullptr) {
                        futuresibs.push_back(node->left);
                        cursum += node->left->val;
                    }
                    if (node->right != nullptr) {
                        futuresibs.push_back(node->right);
                        cursum += node->right->val;
                    }
                    if (!futuresibs.empty()) newlevel.push_back(futuresibs);
                }
            }
            level = newlevel;
        }

        return root;
    }
};