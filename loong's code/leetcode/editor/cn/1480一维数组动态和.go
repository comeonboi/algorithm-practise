package main

func runningSum(nums []int) []int {
	for index := 1; index < len(nums); index++ {
		nums[index] += nums[index-1]
	}
	return nums
}
