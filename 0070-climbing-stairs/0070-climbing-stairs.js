/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {
     if (n <= 2) return n;
        
        let n2 = 1, n1 = 2, all = 0;
        
        for(let i = 2; i < n; i++){
            all = n2 + n1;
            n2 = n1;
            n1 = all;
        }
        return all;
    }
