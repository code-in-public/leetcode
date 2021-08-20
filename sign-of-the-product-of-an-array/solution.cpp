#include <iostream>
#include <vector>

using namespace std;

class Solution {
    public:
        int arraySign(vector<int>& nums) {
            int neg_count = 0;
            for ( int num : nums ) {
                if ( num == 0 ) {
                    return 0;
                }

                if ( num < 0 ) {
                    neg_count++;
                }
            }

            if ( neg_count % 2 == 0 ) {
                return 1;
            } else {
                return -1;
            }
        }
};

int main() {
    cout << "Hello, World!" << endl;

    vector<int> nums{-1, -2, -3, -4, 3, 2, 1};

    /*
    ** Example 1:
        Input: nums = [-1,-2,-3,-4,3,2,1]
        Output: 1
        Explanation: The product of all values in the array is 144, and signFunc(144) = 1

        Example 2:

        Input: nums = [1,5,0,2,-3]
        Output: 0
        Explanation: The product of all values in the array is 0, and signFunc(0) = 0

        Example 3:

        Input: nums = [-1,1,-1,1,-1]
        Output: -1
        Explanation: The product of all values in the array is -1, and signFunc(-1) = -1
    */

    Solution sol;
    cout << sol.arraySign(nums) << endl;
}
