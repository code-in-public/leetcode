#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        vector<int> dp(prices.size());
        dp[0] = 0;
        for (int day = 1; day < prices.size(); day++) {
            dp[day] = dp[day-1] + max(0, prices[day] - prices[day-1]);
        }

        return dp[prices.size()-1];
    }
};

int main() {
    cout << "Solution" << endl;
    vector<int> prices{ 7,1,5,3,6,4 };
    Solution sol;

    cout << sol.maxProfit(prices) << endl;
}
