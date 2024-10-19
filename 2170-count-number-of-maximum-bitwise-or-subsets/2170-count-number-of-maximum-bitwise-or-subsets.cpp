class Solution {
public:
    int countMaxOrSubsets(vector<int>& nums) {
        int maxor = 0;
        for (int n: nums) {
            maxor |= n;
        }

        int total = 0;
        for (int i = 0; i < pow(2, nums.size()); i++) {
            int curror = 0;
            int currnum = i;
            int curri = 0;
            while (currnum) {
                if (currnum % 2 == 1) {
                    curror |= nums[curri];
                }
                currnum >>= 1;
                curri++;
            }
            if (curror == maxor) total++;
        }
        return total;
    }
};