#include <bits/stdc++.h>
using namespace std;

// Function to calculate minimum time required to rot all fresh oranges
int orangesRotting(vector<vector<int>>& grid) {
    
    // If the grid is empty, return 0 as no oranges exist
    if (grid.empty()) return 0;
    
    // Get number of rows and columns in the grid
    int m = grid.size();
    int n = grid[0].size();

    // Variable to store the number of minutes passed
    int days = 0;

    // Variable to store total number of oranges (fresh + rotten)
    int tot = 0;

    // Variable to count how many oranges became rotten during the process
    int cnt = 0;

    // Queue to store positions of currently rotten oranges
    queue<pair<int, int>> rotten;

    // Traverse the grid to count total oranges and push rotten ones to the queue
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            
            // If the cell is not empty (has fresh or rotten orange)
            if (grid[i][j] != 0)
                tot++; // Count it as a valid orange

            // If it's a rotten orange, add its position to the queue
            if (grid[i][j] == 2)
                rotten.push({i, j});
        }
    }

    // Arrays to explore the 4 directions: right, left, down, up
    int dx[4] = {0, 0, 1, -1};
    int dy[4] = {1, -1, 0, 0};

    // BFS traversal until all possible fresh oranges are rotted
    while (!rotten.empty()) {
        
        // Number of rotten oranges to process at this minute
        int k = rotten.size();

        // Add these many oranges to the count of rotted oranges
        cnt += k;

        // Process all rotten oranges at this time step
        while (k--) {
            
            // Get the front orange from the queue
            int x = rotten.front().first;
            int y = rotten.front().second;
            rotten.pop();

            // Check all 4 directions
            for (int i = 0; i < 4; ++i) {
                int nx = x + dx[i]; // New x-coordinate
                int ny = y + dy[i]; // New y-coordinate

                // Skip invalid coordinates or already rotten/empty cells
                if (nx < 0 || ny < 0 || nx >= m || ny >= n || grid[nx][ny] != 1)
                    continue;

                // Mark the fresh orange as rotten
                grid[nx][ny] = 2;

                // Add its position to the queue to process in the next minute
                rotten.push({nx, ny});
            }
        }

        // If new oranges were added to the queue, increase the time
        if (!rotten.empty())
            days++;
    }

    // If all oranges are rotted, return total minutes passed
    // Otherwise, some fresh oranges are left unreachable, return -1
    return tot == cnt ? days : -1;
}

