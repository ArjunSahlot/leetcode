class Solution {
public:
    int finalValueAfterOperations(vector<string>& operations) {
        int ans = 0;
        
        for (const auto& op: operations) {
            switch (op[1]) {
                case '-': ans--; break;
                case '+': ans++; break;
            }
        }
        
        return ans;
    }
};