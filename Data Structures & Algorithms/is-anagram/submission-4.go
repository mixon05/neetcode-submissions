func isAnagram(s string, t string) bool {
    if len(s) != len(t) {
        return false
    }

    m := make(map[rune]int)
    for _, ch := range s {
        m[ch]++
    }
    for _, ch := range t {
        if v, ok := m[ch]; ok && v>0 {
            m[ch]--
        } else {
            return false
        }
    }
    return true
}
