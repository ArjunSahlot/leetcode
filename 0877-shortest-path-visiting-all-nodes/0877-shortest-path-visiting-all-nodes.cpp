class Solution {
public:
    int shortestPathLength(vector<vector<int>>& graph) {
        int n = graph.size();
        // Trivial Case
        if (n == 1) return 0;

        // Visitability DP array indexed via [i, K]
        // where K is an arbitary subset where each bit
        // defines inclusion / exclusion of vertex,
        // and ending its path at vertex i.
        vector<vector<bool>> vis(n, vector<bool>(1<<n, false));
        int t = 1;
        int s = n;
        // Bitmask
        int nMsk;
        // BFS Queue
        queue<pair<int, int>> q;
        // Add all subsets 1 node large
        for (int i = 0; i < n; ++i) q.push({i, 1<<i});
        // Run BFS
        while (q.size()) {
            for (; s;--s, q.pop()) {
                auto& [cNd, msk] = q.front();
                // Visit all neighbors
                for (auto& e : graph[cNd]) {
                    // Mask to determine if 
                    nMsk = msk | (1 << e);
                    // Full Mask Identified, Return Minimium Cost
                    if ((nMsk+1) == (1<<n)) return t;
                    // Already visited in past, do not return
                    if (vis[e][nMsk]) continue;
                    vis[e][nMsk] = true;
                    q.push({e, nMsk});
                }
            }
            s = q.size();
            ++t;
        }
        return 0;
    }
};