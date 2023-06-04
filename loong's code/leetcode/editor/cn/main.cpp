//
// Created by longs on 2023/4/11.
//

#include "main.h"
#include "[977]Squares of a Sorted Array.cpp"
using namespace std;
int main(){
    vector nums = {-4,-1,0,3,10};
    nums = Solution().sortedSquares(nums);
    for (int i = 0; i < nums.size(); ++i) {
        cout<<nums[i]<<endl;
    };
}