package main

func minSubArrayLen(target int, nums []int) int {
	n := len(nums)
	ans := n + 1
	s := 0
	left := 0
	for right, x := range nums {
		s += x
		for s >= target {
			ans = min(ans, right-left+1)
			s -= nums[left]
			left += 1
		}
	}
	if ans <= n {
		return ans
	}
	return 0
}

func min(a, b int) int {
	if a > b {
		return b
	}
	return a
}
