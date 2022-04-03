class Solution {
public:
    int maximumWealth(vector<vector<int>>& accounts) {
        int max = 0;
        
        for (const auto& sub: accounts) {
            int sum = 0;
            for (const auto& i: sub) {
                sum += i;
            }
            if (sum > max) max = sum;
        }
        
        return max;
    }
};