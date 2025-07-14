class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        
        std::unordered_map<int,int>f;
        for(int num : nums)
            {
                f[num]++;
                 
                if(f[num]>1)
                {
                    return true;
                }
            }
        return false;
    }
};