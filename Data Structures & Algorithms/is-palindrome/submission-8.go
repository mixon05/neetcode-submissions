func isPalindrome(s string) bool {
    s = formatString(s)
    if len(s) <= 1 {
        return true
    }
    var middle int = len(s) / 2
    for i:=0; i<=middle; i++ {
        if s[i] != s[len(s)-1-i] {
            return false
        }
    }
    return true
}

func formatString(s string) string {
    var result string
    for _, c := range s {
        if c >= 'a' && c <= 'z' {
            result += string(c)
        } else if c >= 'A' && c <= 'Z' {
            result += string(c + 'a' - 'A')
        } else if c >= '0' && c <= '9' {
            result += string(c)
        }
    }
    return result
}
