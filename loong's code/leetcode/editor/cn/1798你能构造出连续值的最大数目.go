package main

import "sort"

func getMaximumConsecutive(coins []int) int {
	// 初始化一个包含0的数组
	m := 0
	sort.Ints(coins)
	for _, c := range coins {
		if c > m+1 {
			break
		}
		m += c
	}
	return m + 1
}
