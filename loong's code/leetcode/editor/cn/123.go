package main

func a(x []int) []int {
	for i := 0; i < len(x); i++ {
		if i%2 == 0 {
			x[i] = 1
		}
	}
	return x
}
