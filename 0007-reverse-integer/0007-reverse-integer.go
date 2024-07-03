import "math"

func reverse(x int) int {
    var isNegative bool
    if x < 0 {
        isNegative = true
        x *= -1
    }
    
    var res int64 = 0
    
    for x > 0 {
        res = 10 * res + int64(x % 10)
        x = x / 10
    }
    
    if isNegative {
        res *= -1
    }
    
    if res > math.MaxInt32 || res < math.MinInt32 {
        return 0
    }
    
    return int(res)
}