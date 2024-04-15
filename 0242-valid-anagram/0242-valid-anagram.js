/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    if (s.length != t.length){
        return false
    }
    obj = {}
    
    for (let i = 0;i<s.length;i++){
        if (obj[s[i]]){
            obj[s[i]] += 1
            continue
        }
        obj[s[i]] = 1
    }
    
    console.log(obj)
    for (let i = 0;i<t.length;i++){
        if (!obj[t[i]]){
            return false
        }
        obj[t[i]] -= 1
    }
    
    for (let k in obj){
        if (obj[k] != 0) return false
    }
    
    
    
    return true
};