// problem statement: check if frequency can be equal
class Solution {
    
    boolean isSame(int[] freq, int size) {
        int c=0;
        int i=0;
        for (i=0; i<size; ++i){
            if (freq[i]>0){
                c= freq[i];
                break;
            }
        }
        
        for(int j = i + 1; j<size; ++j ){
            if (freq[j]>0 && freq[j] !=c){
                return false;
            }
        }
        
        return true;
    }
    
    boolean sameFreq(String s) {
        int[] freq = new int[26];
        for(char c: s.toCharArray()){
            freq[c-'a']++;
        }
        if (isSame(freq,26)){
            return true;
        }
        for(int i=0; i<26; ++i){
            if (freq[i]>0){
                freq[i]--;
                if (isSame(freq,26)){
                    return true;
                }
                freq[i]++;
            }
        }
        return false;
    }
}
