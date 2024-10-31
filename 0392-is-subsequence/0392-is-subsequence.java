class Solution {
    public boolean isSubsequence(String s, String t) {
       if(t.length() < s.length()){
            return false;
        }
        
        if(s.isBlank()){
            return true;
        }
        
        int i = 0, l = 0;
        
        while (l < t.length()){
            if (s.charAt(i) == t.charAt(l)) i++;
            
            if (i == s.length()) return true;
            
            l++;
        }
        
        return false;
    }
}