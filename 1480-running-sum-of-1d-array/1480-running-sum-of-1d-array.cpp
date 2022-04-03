class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        int sum = 0;
        vector<int> rv;
        for (const auto& i: nums) {
            sum += i;
            rv.push_back(sum);
        }
        return rv;
    }
};