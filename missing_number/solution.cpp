class Solution {
public:
    int missingNumber(vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        for (auto i = 0; i < nums.size(); i++) if (nums[i] != i) return i;
        return nums.size();
    }
};
