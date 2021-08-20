#include <iostream>
#include <vector>

using namespace std;

int main() {
    vector<int> values = {1, 5, 7, 2, 9, 4};

    // Find biggest value
    // Current list, biggest
    // [1] = 1
    // [1, 5] = 5
    // [1, 5, 7] = 7
    //
    // dp = [1, 5, ...]
    //
    // dp[i] = max(values[i], dp[i-1])
}
