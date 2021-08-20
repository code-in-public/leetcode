#include <iostream>
#include <vector>

using namespace std;

int get_max_recursive(vector<int> &values, int start_idx) {
    if (start_idx == values.size()-1) {
       return values[start_idx];
    }

    return max(values[start_idx], get_max_recursive(values, start_idx + 1));
}

int main() {
    { //Start of scope
        // This is a new scope

        int x = 5;

        {
            int* y = new int();
        }
    }
    cout << "Hello" << endl;

    // Get the max value for a given vector
    vector<int> values = {1, 9, 3, 5, 7, 5, 1, 4};

    cout << get_max_recursive(values, 0) << endl;
}

// About 2mb of stack memory
// Contiguous memory
// [start_of_my_scope_1,  int for x,  start_of_scope_2, int* y address of int in the heap          ]

// A lot heap memory


int dp() {
    vector<int> prices = {1, 2, 3, 4, 2};

    // [0, 1, 1 + 1 = 2, 1 + 1 + dp[i-1]]
    //
    // dp[i] = dp[i-1] + max(0, prices[i] - prices[i-1])
}
