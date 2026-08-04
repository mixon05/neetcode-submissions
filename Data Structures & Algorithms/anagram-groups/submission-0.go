func groupAnagrams(strs []string) [][]string {
	m := make(map[[26]int][]string)

	for _, str := range strs {
		var count [26]int
		for _, char := range str {
			count[char-'a']++
		}
		m[count] = append(m[count], str)
	}

	result := make([][]string, 0, len(m))
	for _, group := range m {
		result = append(result, group)
	}

	return result
}