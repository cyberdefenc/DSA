import java.util.Arrays;

public class P1_twosum_ {
    public static void main(String[] args) {
       
        int[] nums = {2, 7, 11, 15};
        int target = 9;

        // Create an instance of Solution class
        Solution solution = new Solution();

        // Call the twoSum method
        int[] result = solution.twoSum(nums, target);

        
        System.out.println("Indices of numbers that sum to " + target + " are: " + Arrays.toString(result));
    }
}


class Solution {
    public int[] twoSum(int[] nums, int target) {
        for(int i = 0; i < nums.length - 1; i++) {
            for(int j = i + 1; j < nums.length; j++) {
                if(nums[i] + nums[j] == target) {
                    return new int[]{i, j};
                }
            }
        }
        return new int[]{}; // fallback if no pair found (won’t happen here)
    }
}
