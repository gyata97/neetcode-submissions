class Solution {
    public boolean isAnagram(String s, String t) {
        Map<Character, Integer> mp = new HashMap<>();

        for(int i = 0; i < s.length(); i++){
            int count = mp.getOrDefault(s.charAt(i), 0) + 1;
            mp.put(s.charAt(i), count);
        }

        for(int i = 0; i < t.length(); i++){
            int count = mp.getOrDefault(t.charAt(i), 0) - 1;
            mp.put(t.charAt(i), count);
        }

        for(Map.Entry<Character, Integer> entry: mp.entrySet()){
            if(entry.getValue() != 0){
                return false;
            }
        }

        return true;
    }
}
