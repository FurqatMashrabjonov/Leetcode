func twoSum(nums []int, target int) []int {
    for i, _ := range nums {
        for j := i + 1; j < len(nums);j += 1 {
            if nums[i] + nums[j] == target {
                return []int{i, j}
            }
        }
    }
    return []int{}
}