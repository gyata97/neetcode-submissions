class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> mp = new HashMap<>();

        for(int i = 0; i < nums.length; i++){
            int toFind = target - nums[i];
            if(mp.containsKey(toFind)){
                return new int[]{mp.get(toFind), i};
            }
            mp.put(nums[i], i);
        }

        return new int[] {-1,-1};
    }
}
