package main

func numberOfSteps(num int) int {
	var count = 0
	if num == 0 {
		return 0
	}
	for {
		if num == 2 {
			count += 2
			break
		}
		if num == 1 {
			count += 1
			break
		}
		if num%2 == 0 {
			count += 1
		} else {
			count += 2
		}
		num = num / 2
	}
	return count
}
