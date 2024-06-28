func twoSum(nums []int, target int) []int {
    hash := make(map[int]int)
    
    for i, v := range nums {
        if val, ok := hash[v]; ok {
            return []int{val, i}
        }
        hash[target - v] = i
    }
    
    
    return []int{}
}