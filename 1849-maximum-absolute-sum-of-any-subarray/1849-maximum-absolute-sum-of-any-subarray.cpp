class Solution {
public:
    int maxAbsoluteSum(vector<int>& nums) {
        // DP[i] = largest sum that ends at nums_i
        int curmax = 0;

        vector<int> dpp(nums.size(), 0);
        dpp[0] = max(0, nums[0]);
        for (int i = 1; i < nums.size(); i++) {
            if (dpp[i-1]+nums[i] < 0) {
                dpp[i] = 0;
            } else {
                dpp[i] = dpp[i-1] + nums[i];
            }
            curmax = max(dpp[i], curmax);
        }

        // DP[i] = smallest sum that ends at nums_i
        vector<int> dpn(nums.size(), 0);
        dpn[0] = min(0, nums[0]);
        for (int i = 1; i < nums.size(); i++) {
            if (dpn[i-1] + nums[i] > 0) {
                dpn[i] = 0;
            } else {
                dpn[i] = dpn[i-1] + nums[i];
            }
            curmax = max(abs(dpn[i]), curmax);
        }

        return max(curmax, abs(nums[0]));
    }
};