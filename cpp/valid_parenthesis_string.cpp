#include <iostream>
#include <string>
#include <stack>

class Solution {
public:
    bool checkValidString(std::string s) {
        if (s.length() == 0) return true;

        std::stack<int> left_stack, right_stack, star_stack;
        char current_char;

        // preprocessing
        for(int i = 0; i < s.length(); i++) {
            current_char = s[i];
            if (current_char == '(') left_stack.push(i);
            else if (current_char == ')') {
                if (left_stack.size() == 0 && star_stack.size() == 0) return false;
                if (left_stack.size()) left_stack.pop();
                else if (!left_stack.size() && star_stack.size()) right_stack.push(i);
            } else star_stack.push(i);
        }

        // post processing
        int idx, star_index;
        if (!left_stack.empty()) {
            
            while(!left_stack.empty() && !star_stack.empty()) {
                idx = left_stack.top();
                star_index = star_stack.top();
                star_stack.pop();
                if (idx < star_index) left_stack.pop();
            }
        }

        if (!right_stack.empty()) {
            while (!right_stack.empty() && !star_stack.empty()) {
                idx = right_stack.top();
                star_index = star_stack.top();
                star_stack.pop();
                if (star_index < idx) right_stack.pop();
            }
        }

        return left_stack.empty() && right_stack.empty();
    }
};

int main() {
    Solution solution = Solution();
    std::cout << solution.checkValidString("(())") << std::endl;

    return 0;
}
