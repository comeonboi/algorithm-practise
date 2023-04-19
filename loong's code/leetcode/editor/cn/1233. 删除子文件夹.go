package main

import "sort"

func removeSubfolders(folder []string) (ans []string) {
	sort.Strings(folder)
	ans = []string{folder[0]}
	for _, i := range folder[1:] {
		m, n := len(ans[len(ans)-1]), len(i)
		if m >= n || !(ans[len(ans)-1] == i[:m] && i[m] == '/') {
			ans = append(ans, i)
		}
	}
	return
}
