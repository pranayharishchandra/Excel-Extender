#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    // Computes the count of land cells not reachable from boundary (enclaves)
    int numberOfEnclaves(vector<vector<int>>& grid) {
        // Handle empty grid
        if (grid.empty() || grid[0].empty()) return 0;

        // Fetch dimensions
        int n = (int)grid.size();
        int m = (int)grid[0].size();

        // Create visited matrix initialized to 0
        vector<vector<int>> vis(n, vector<int>(m, 0));

        // Create a queue for BFS
        queue<pair<int,int>> q;

        // Traverse all boundary cells and enqueue boundary lands
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                // Check if current cell lies on boundary
                if (i == 0 || j == 0 || i == n - 1 || j == m - 1) {
                    // If boundary cell is land, mark visited and push to queue
                    if (grid[i][j] == 1) {
                        vis[i][j] = 1;
                        q.push({i, j});
                    }
                }
            }
        }

        // Direction vectors for 4-neighborhood
        int delrow[] = {-1, 0, +1, 0};
        int delcol[] = {0, +1, 0, -1};

        // BFS to mark all land cells reachable from boundary
        while (!q.empty()) {
            auto [row, col] = q.front();
            q.pop();

            // Explore four directions
            for (int k = 0; k < 4; k++) {
                int nrow = row + delrow[k];
                int ncol = col + delcol[k];

                // Check bounds, unvisited, and land
                if (nrow >= 0 && nrow < n && ncol >= 0 && ncol < m
                    && !vis[nrow][ncol] && grid[nrow][ncol] == 1) {
                    vis[nrow][ncol] = 1;
                    q.push({nrow, ncol});
                }
            }
        }

        // Count land cells that are not visited (i.e., enclaves)
        int cnt = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == 1 && vis[i][j] == 0) cnt++;
            }
        }
        return cnt;
    }
};

int main() {
    // Define the grid
    vector<vector<int>> grid{
        {0, 0, 0, 0},
        {1, 0, 1, 0},
        {0, 1, 1, 0},
        {0, 0, 0, 0}
    };

    // Create Solution instance
    Solution obj;

    // Compute and print the number of enclaves
    cout << obj.numberOfEnclaves(grid) << endl; // Expected: 3
    return 0;
}
