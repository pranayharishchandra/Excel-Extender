// In this BFS approach, using bool for vis and color is more intuitive and memory-efficient.
class Solution {
public:
    // Check if any component is Bipartite using BFS
    bool bfs(int node, vector<vector<int>>& graph, vector<bool>& color, vector<bool>& vis) {
        queue<int> q;
        q.push(node);
        vis[node]   = true;
        color[node] = true; // Start coloring with true
        
        while (!q.empty()) {
            int curr = q.front();
            q.pop();
            
            for (int adjNode : graph[curr]) {
                if (!vis[adjNode]) {
                    // Assign opposite color to the adjacent node
                    color[adjNode] = !color[curr];
                    vis[adjNode] = true;
                    q.push(adjNode);
                } 
                else if (color[adjNode] == color[curr]) {
                    // If adjacent nodes have the same color, it's not bipartite
                    return false;
                }
            }
        }
        
        return true;
    }

    bool isBipartite(vector<vector<int>>& graph) {
        int n = graph.size();
        vector<bool> color(n, false); // Initial color of all nodes
        vector<bool> vis(n, false);   // Visited array
        
        // Check each component of the graph
        for (int i = 0; i < n; ++i) {
            if (!vis[i] && !bfs(i, graph, color, vis)) {
                return false; // If any component is not bipartite, return false
            }
        }
        
        return true;
    }
};