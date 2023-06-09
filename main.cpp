//
// Created by longs on 2023/4/19.
//
//
// Created by longs on 2023/4/11.
//

#include "loong's code/leetcode/editor/cn/main.h"
#include "loong's code/leetcode/editor/cn/[977]Squares of a Sorted Array.cpp"
using namespace std;
int main(){
    vector nums = {-4,-1,0,3,10};
    nums = Solution().sortedSquares(nums);
    for (int num : nums) {
        cout<<num<<endl;
    };
}