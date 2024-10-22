class Solution {
public:
    unordered_map<char, vector<string>> mapping = {
        {'2', {"a", "b", "c"}},
        {'3', {"d", "e", "f"}},
        {'4', {"g", "h", "i"}},
        {'5', {"j", "k", "l"}},
        {'6', {"m", "n", "o"}},
        {'7', {"p", "q", "r", "s"}},
        {'8', {"t", "u", "v"}},
        {'9', {"w", "x", "y", "z"}}
    };
    vector<string> letterCombinations(string digits) {
        if (digits.size() == 0) {
            return vector<string>();
        }
        if (digits.size() == 1) {
            return mapping[digits[0]];
        }
        vector<string> prevCombs = letterCombinations(digits.substr(1));
        vector<string> currCombs;
        for (string prefix: mapping[digits[0]]) {
            for (string comb: prevCombs) {
                currCombs.push_back(prefix + comb);
            }
        }
        return currCombs;
    }
};