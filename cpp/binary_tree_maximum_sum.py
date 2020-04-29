#include <iostream>
#include <stack>
#include <tuple>
#include <limits>
#include <unordered_map>

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

typedef std::tuple<TreeNode*, TreeNode*, int> node;

class Solution {
public:
    int maxPathSum(TreeNode* root) {
        if (!root) return 0;

        int max = INT32_MIN;
        std::stack<node> stack1, stack2;
        std::unordered_map<TreeNode*, int> left, right;
        stack1.push(std::make_tuple(root, nullptr, -1));

        while (!stack1.empty()) {
            node current_tuple = stack1.top();
            stack1.pop();
            stack2.push(current_tuple);
            TreeNode* parent = std::get<0>(current_tuple);
            if (parent->left) 
                stack1.push(std::make_tuple(parent->left, parent, 0));
            if (parent->right)
                stack1.push(std::make_tuple(parent->right, parent, 1));
        }

        while (!stack2.empty()) {
            node current_tuple = stack2.top();
            stack2.pop();
            int left_max = 0, right_max = 0;
            TreeNode* current_node = std::get<0>(current_tuple);
            TreeNode* parent_node = std::get<1>(current_tuple);
            if (left.find(current_node) != left.end()) left_max = left.at(current_node);
            if (right.find(current_node) != right.end()) right_max = right.at(current_node);
            if (parent_node) {
                if (std::get<2>(current_tuple) == 0) left[parent_node] = std::max(std::max(current_node->val+left_max, current_node->val+right_max), current_node->val);
                else right[parent_node] = std::max(std::max(current_node->val+left_max, current_node->val+right_max), current_node->val);
            }
            
            max = std::max(max, std::max(std::max(current_node->val+left_max, current_node->val+right_max), std::max(current_node->val, current_node->val+left_max+right_max)));
        }
        return max;
    }
};