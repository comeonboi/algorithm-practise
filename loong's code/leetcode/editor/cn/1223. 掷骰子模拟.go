package main

// 会超时的回溯写法
func dieSimulator(n int, rollMax []int) (ans int) {
	const mod int = 1e9 + 7

	const m = 6
	cache := make([][m][]int, n)
	for i := range cache {
		for j := range cache[i] {
			cache[i][j] = make([]int, rollMax[j])
			for k := range cache[i][j] {
				cache[i][j][k] = -1
			}
		}
	}

	var dfs func(int, int, int) int
	dfs = func(i, last, left int) (res int) {
		if i == 0 {
			return 1
		}
		for j, mx := range rollMax {
			if j != last {
				res += dfs(i-1, j, mx-1)
			} else if left > 0 {
				res += dfs(i-1, j, left-1)
			}
		}
		return res % mod
	}
	for j, mx := range rollMax {
		ans += dfs(n-1, j, mx-1)
	}
	return ans % mod
}
