#include <iostream>
#include <vector>

using namespace std;

class Solution {
    public:
        int maxProfit(vector<int>& prices) {
            // For each day, identify max profit if we sold on that day
            // Finding the smallest value before this day
            //         1 2 3 4 5 6 7 8
            // Prices {3,3,5,0,0,3,1,4};
            //   dp[0]{0,0,2,2,2,3,3,4|};
            //   dp[1]{0,0,2,2,2,3,3,|3};
            //   dp[2]{0,0,2,2,2,3,|3,3};
            //   dp[3]{0,0,2,2,2,|2,2,4};
            //   dp[4]{0,0,2,2,|0,3,3,4};
            //   dp[5]{0,0,2,|0,2,3,3,4};
            //   dp[6]{0,0,|0,2,2,3,3,4};
            //   dp[7]{0,|0,2,2,2,3,3,4};
            //
            // Start with a DP for a single pruchase
            // DP contains the max profit if we sold on the i-th day
            // Figure out the max profit for a second purchase
            //   Second puchase happens ofter j-th day
            //   size-j = 0, populate the rest of the dp for j-th row
            return -1;
    }
};

int main() {
    Solution sol;

    vector<int> prices{3,3,5,0,0,3,1,4};
    //Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3),
    //profit = 3-0 = 3.
    // Then buy on day 7 (price = 1) and sell on day 8 (price = 4),
    // profit = 4-1 = 3.
    cout << sol.maxProfit(prices) << endl;
}
