package main

func checkXMatrix(grid [][]int) bool {
	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid[i]); j++ {
			//第一行的俩数字
			if (i == j) || (i+j == len(grid)-1) {
				if grid[i][j] == 0 {
					return false
				}

			} else if grid[i][j] != 0 {
				return false
			}
		}
	}
	return true
}
