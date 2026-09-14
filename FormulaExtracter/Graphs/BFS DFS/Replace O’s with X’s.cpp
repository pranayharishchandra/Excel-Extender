#include <bits/stdc++.h>
using namespace std;

class Solution {
private:
    // DFS to mark boundary-connected 'O's as visited
    void dfs(int row, int col, vector<vector<int>>& vis, vector<vector<char>>& mat, int delrow[], int delcol[]) {
        // mark current cell visited
        vis[row][col] = 1;
        // cache dimensions
        int n = mat.size(), m = mat[0].size();
        // try 4 directions
        for (int k = 0; k < 4; k++) {
            // compute next cell
            int nrow = row + delrow[k], ncol = col + delcol[k];
            // check bounds and unvisited 'O'
            if (nrow >= 0 && nrow < n && ncol >= 0 && ncol < m && !vis[nrow][ncol] && mat[nrow][ncol] == 'O') {
                // continue DFS
                dfs(nrow, ncol, vis, mat, delrow, delcol);
            }
        }
    }

public:
    // Flip all 'O' not connected to boundary to 'X'
    vector<vector<char>> fill(int n, int m, vector<vector<char>> mat) {
        // handle empty matrix
        if (n == 0 || m == 0) return mat;
        // direction arrays for 4-neighbors
        int delrow[4] = {-1, 0, 1, 0};
        int delcol[4] = {0, 1, 0, -1};
        // visited matrix
        vector<vector<int>> vis(n, vector<int>(m, 0));

        // traverse first and last row
        for (int j = 0; j < m; j++) {
            // start DFS from unvisited boundary 'O' (top row)
            if (!vis[0][j] && mat[0][j] == 'O') dfs(0, j, vis, mat, delrow, delcol);
            // start DFS from unvisited boundary 'O' (bottom row)
            if (!vis[n - 1][j] && mat[n - 1][j] == 'O') dfs(n - 1, j, vis, mat, delrow, delcol);
        }

        // traverse first and last column
        for (int i = 0; i < n; i++) {
            // start DFS from unvisited boundary 'O' (left col)
            if (!vis[i][0] && mat[i][0] == 'O') dfs(i, 0, vis, mat, delrow, delcol);
            // start DFS from unvisited boundary 'O' (right col)
            if (!vis[i][m - 1] && mat[i][m - 1] == 'O') dfs(i, m - 1, vis, mat, delrow, delcol);
        }

        // flip all unvisited 'O' to 'X'
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                // convert enclosed 'O' to 'X'
                if (!vis[i][j] && mat[i][j] == 'O') mat[i][j] = 'X';
            }
        }

        // return updated board
        return mat;
    }
};

int main() {
    // sample board
    vector<vector<char>> mat{
        {'X','X','X','X'},
        {'X','O','X','X'},
        {'X','O','O','X'},
        {'X','O','X','X'},
        {'X','X','O','O'}
    };
    // create solver
    Solution ob;
    // compute result
    vector<vector<char>> ans = ob.fill((int)mat.size(), (int)mat[0].size(), mat);
    // print board
    for (int i = 0; i < (int)ans.size(); i++) {
        for (int j = 0; j < (int)ans[0].size(); j++) {
            cout << ans[i][j] << " ";
        }
        cout << "\n";
    }
    return 0;
}
