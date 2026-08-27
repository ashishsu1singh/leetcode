class Solution {
public:
    bool isMiddleElementUnique(vector<int>& nums) {
        int n=nums.size(),mid=nums[n/2],res=0;
        for(int i=0;i<n;i++)
        {
            if(nums[i]==mid){
                res++;
            }
        }
        return res==1;
    }
};