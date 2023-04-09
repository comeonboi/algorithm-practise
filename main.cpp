//
// Created by longs on 2023/4/9.
//
#include<iostream>
#include "vector"
#include "loong's code/leetcode/editor/cn/[27]Remove Element.cpp"
using namespace std;
int main(){
    vector<int> nums = {0,1,2,2,3,0,4,2};
    cout<<(new Solution())->removeElement(nums, 2)<<endl;
}