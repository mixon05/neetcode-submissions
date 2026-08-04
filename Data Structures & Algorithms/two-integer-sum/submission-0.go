func twoSum(nums []int, target int) []int {
    m := make(map[int]int)
    for idx2, num := range nums {
        remainder := target - num
        if idx1, ok := m[remainder]; ok {
             return []int{idx1,idx2}
        }
        m[num] = idx2
    }
    return nil
}
