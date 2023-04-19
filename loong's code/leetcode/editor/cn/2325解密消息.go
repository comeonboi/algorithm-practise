package main

func decodeMessage(key string, message string) string {
	mp := ['z' + 1]byte{' ': ' '}
	cur := byte('a')
	for _, c := range key {
		if mp[c] == 0 {
			mp[c] = cur
			cur += 1
		}
	}
	s := []byte(message)
	for i, c := range s {
		s[i] = mp[c]
	}
	return string(s)
}
