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
    bool flipEquiv(TreeNode* root1, TreeNode* root2) {
        if (root1 == nullptr) return root2 == nullptr;
        if (root2 == nullptr) return root1 == nullptr;
        if (root1->val != root2->val) return false;

        if (root1->left == nullptr && root1->right == nullptr) {
            return root2->left == nullptr && root2->right == nullptr;
        }

        if (root1->left != nullptr && root1->right == nullptr) {
            if (root2->left != nullptr && root2->right != nullptr) return false;
            if (root2->left == nullptr && root2->right == nullptr) return false;
            if (root2->left != nullptr) return flipEquiv(root1->left, root2->left);
            if (root2->right != nullptr) return flipEquiv(root1->left, root2->right);
        }

        if (root1->left == nullptr && root1->right != nullptr) {
            if (root2->left != nullptr && root2->right != nullptr) return false;
            if (root2->left == nullptr && root2->right == nullptr) return false;
            if (root2->left != nullptr) return flipEquiv(root1->right, root2->left);
            if (root2->right != nullptr) return flipEquiv(root1->right, root2->right);
        }

        if (root2->left == nullptr || root2->right == nullptr) return false;

        if (root1->left->val == root2->left->val) {
            if (root1->right->val != root2->right->val) return false;
            return flipEquiv(root1->left, root2->left) && flipEquiv(root1->right, root2->right);
        }

        if (root1->left->val == root2->right->val) {
            if (root1->right->val != root2->left->val) return false;
            return flipEquiv(root1->left, root2->right) && flipEquiv(root1->right, root2->left);
        }

        return false;
    }
};