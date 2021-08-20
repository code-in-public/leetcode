#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

class Solution {
    /*
    ** Followers:
    ** ForeGATHERS
    ** beefviper
    ** iDreamHigh
    ** Da_verox
    */
    private:
        double get_distance(double x1, double y1, double x2, double y2) {
            // sqrt((x1 - x2)^2 + (y1-y2)^2)
            return (pow(x1-x2, 2) + pow(y1-y2, 2));
        }
    public:
        /*
        ** Return the number of point inside each of the query circles
         */
        vector<int> countPoints(vector<vector<int>>& points, vector<vector<int>>& queries) {
            vector<int> result(queries.size(), 0);

            // For each of the queries, check each of the points to find which are in range
            int size = result.size();
            for (int i = 0; i < size; i++) {
                // Check if the point is close enough to the circles center
                int circle_x = queries[i][0];
                int circle_y = queries[i][1];
                int circle_r = queries[i][2];

                for (auto& point : points) {
                    int point_x = point[0];
                    int point_y = point[1];

                    if ( get_distance(circle_x, circle_y, point_x, point_y) <= pow(circle_r, 2 )) {
                        result[i]++;
                    }
                }
            }

            return result;
        }
};

int main() {
    /*
    ** Input: points = [[1,3],[3,3],[5,3],[2,2]], queries = [[2,3,1],[4,3,1],[1,1,2]]
Output: [3,2,2]
    */

    vector<vector<int>> points{{1, 3}, {3, 3}, {5, 3}, {2, 2}};
    vector<vector<int>> queries{{2, 3, 1}, {4, 3, 1}, {1, 1, 2}};

    Solution sol;

    vector<int> results = sol.countPoints(points, queries);

    for (auto result : results) {
        cout << result << endl;
    }
}
