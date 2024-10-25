class Solution {
public:
    double frogPosition(int n, vector<vector<int>>& edges, int t, int target) {
        unordered_map<int, vector<int>> graph;
        for (auto e: edges) {
            graph[e[0]].push_back(e[1]);
            graph[e[1]].push_back(e[0]);
        }

        vector<double> probs(n+1, 0);
        probs[0] = 1;
        
        vector<tuple<int, int, int>> neighbors;
        neighbors.push_back({0, 1, 1});
        while (!neighbors.empty()) {
            vector<tuple<int, int, int>> newneighs;
            for (int i = 0; i < neighbors.size(); i++) {
                auto neigh = neighbors[i];
                probs[get<2>(neigh)] = abs(probs[get<0>(neigh)] / (double)get<1>(neigh));
                probs[get<0>(neigh)] = min(-1*probs[get<0>(neigh)], probs[get<0>(neigh)]);

                // add neighs neighbors to newneighs
                vector<int> neighsneighs = graph[get<2>(neigh)];
                int count = 0;
                for (int j = 0; j < neighsneighs.size(); j++) {
                    if (probs[neighsneighs[j]] != 0) continue;
                    count++;
                }

                for (int j = 0; j < neighsneighs.size(); j++) {
                    if (probs[neighsneighs[j]] != 0) continue;
                    newneighs.push_back({get<2>(neigh), count, neighsneighs[j]});
                }
            }

            if (t-- <= 0) break;
            neighbors = newneighs;
        }

        return max(probs[target], (double)0);
    }
};