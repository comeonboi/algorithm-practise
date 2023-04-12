//
// Created by longs on 2023/4/11.
//

#ifndef ALGORITHM_PRACTISE_MAIN_H
#define ALGORITHM_PRACTISE_MAIN_H
#include "vector"
#include "stack"
#include "iostream"
#include "string"
#include <unordered_map>
#include <unordered_set>
using namespace std;
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

#endif //ALGORITHM_PRACTISE_MAIN_H
