

func isPalindrome(s string) bool {
	s = formatString(s)
	n := len(s)

	for i := 0; i < n/2; i++ {
		if s[i] != s[n-1-i] {
			return false
		}
	}
	return true
}

func formatString(s string) string {
	var b strings.Builder
	b.Grow(len(s)) 

	for _, c := range s {
		if c >= 'a' && c <= 'z' || c >= '0' && c <= '9' {
			b.WriteRune(c)
		} else if c >= 'A' && c <= 'Z' {
			b.WriteRune(c + 'a' - 'A')
		}
	}
	return b.String()
}