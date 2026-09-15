#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    // DFS traversal
    void dfs(int row, int col, int baseRow, int baseCol,
             vector<vector<int>>& grid, vector<vector<int>>& vis,
             vector<pair<int, int>>& shape) {
        // Mark as visited
        vis[row][col] = 1;
        // Store relative position
        shape.push_back({row - baseRow, col - baseCol});

        // All 4 directions
        int drow[] = {-1, 0, 1, 0};
        int dcol[] = {0, 1, 0, -1};

        // Explore all directions
        for (int i = 0; i < 4; i++) {
            int nrow = row + drow[i];
            int ncol = col + dcol[i];

            // Check bounds and if land and not visited
            if (nrow >= 0 && nrow < grid.size() &&
                ncol >= 0 && ncol < grid[0].size() &&
                !vis[nrow][ncol] && grid[nrow][ncol] == 1) {
                dfs(nrow, ncol, baseRow, baseCol, grid, vis, shape);
            }
        }
    }

    // Main function to return number of distinct islands
    int countDistinctIslands(vector<vector<int>>& grid) {
        int n = grid.size();
        int m = grid[0].size();
        vector<vector<int>> vis(n, vector<int>(m, 0));
        set<vector<pair<int, int>>> st;

        // Traverse grid
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                // If land and not visited
                if (grid[i][j] == 1 && !vis[i][j]) {
                    vector<pair<int, int>> shape;
                    dfs(i, j, i, j, grid, vis, shape);
                    st.insert(shape);
                }
            }
        }
        return st.size();
    }
};

// Driver code
int main() {
    vector<vector<int>> grid = {
        {1, 1, 0, 0},
        {1, 0, 0, 0},
        {0, 0, 1, 1},
        {0, 0, 1, 1}
    };
    Solution obj;
    cout << obj.countDistinctIslands(grid);
    return 0;
}
