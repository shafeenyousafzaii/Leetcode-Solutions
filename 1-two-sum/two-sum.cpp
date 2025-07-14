class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> no;
        if(nums.size()==2)
            return vector<int> {0,1};
        for(int i=0;i<nums.size();i++)
        {
            for(int j=0;j<nums.size();j++)
            {
                if(nums[i]+nums[j]==target && i!=j)
                {
                    vector<int> hi={i,j};
                    return hi;
                }
            }
        }
        return no;
    }
};