class Solution {
public:
    void sortColors(vector<int>& nums) {
        int left = 0;
        int current = 0;
        int right = nums.size() - 1;
        
        while (current <= right) {
            if (nums[current] == 0){
                swap(nums[current], nums[left]);
                left ++;
                current ++;
            }
            else if (nums[current] == 2){
                swap(nums[current], nums[right]);
                right --;
            }
            else{
                current ++;
            }
        }
    }
};