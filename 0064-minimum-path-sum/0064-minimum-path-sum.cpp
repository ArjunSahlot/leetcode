class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        int optimals[m][n];

        int cursum = 0;
        for (int i = 0; i < n; i++) {
            cursum += grid[0][i];
            optimals[0][i] = cursum;
        }
        cursum = 0;
        for (int i = 0; i < m; i++) {
            cursum += grid[i][0];
            optimals[i][0] = cursum;
        }

        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                optimals[i][j] = grid[i][j] + min(optimals[i-1][j], optimals[i][j-1]);
            }
        }

        return optimals[m-1][n-1];
    }
};