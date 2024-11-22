class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        vector<int> exp;
        for (string s: tokens) {
            if (s == "+") {
                int val = exp[exp.size()-2] + exp[exp.size()-1];
                exp.pop_back();
                exp.pop_back();
                exp.push_back(val);
            } else if (s == "*") {
                int val = exp[exp.size()-2] * exp[exp.size()-1];
                exp.pop_back();
                exp.pop_back();
                exp.push_back(val);
            } else if (s == "-") {
                int val = exp[exp.size()-2] - exp[exp.size()-1];
                exp.pop_back();
                exp.pop_back();
                exp.push_back(val);
            } else if (s == "/") {
                int val = exp[exp.size()-2] / exp[exp.size()-1];
                exp.pop_back();
                exp.pop_back();
                exp.push_back(val);
            } else {
                exp.push_back(stoi(s));
            }
        }

        return exp.back();
    }
};