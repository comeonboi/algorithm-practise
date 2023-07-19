package contest

func convertToTitle(n int) string {
	var result string
	for n > 0 {
		n--
		result = string('A'+n%26) + result
		n /= 26
	}
	return result
}

func main() {
	println(convertToTitle(1))
	println(convertToTitle(28))
	println(convertToTitle(701))
}
