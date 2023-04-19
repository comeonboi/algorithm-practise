package main

import "fmt"

//	func main() {
//		fmt.Println("Hello world")
//		arr := []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
//		fmt.Println(a(arr))
//		fmt.Println(twoSum([]int{2, 7, 11, 15}, 9))
//	}

var counter int

func gcd(m int, n int) int {
	counter++
	if n == 0 {
		return m
	}
	if n > 0 {
		return gcd(n, m%n)
	}
	return 1
}

func main() {
	fmt.Println(gcd(48, 15), counter)
}
