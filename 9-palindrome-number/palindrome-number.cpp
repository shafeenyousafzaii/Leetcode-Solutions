class Solution {
public:
    bool isPalindrome(int x) {
        int loop = std::to_string(x).length();
        string number=std::to_string(x); 
        char *ptr1=&number[0];
        char *ptr2=&number[loop-1];
        bool pal=true;
        if(x<0)
            return false;
        if(x<10 && x>=0)
            return true;
        for (int i=0;i<loop/2;i++)
        {
           if(*ptr1!=*ptr2)
           {
            return false;
           }
           ptr1++;
           ptr2--;
            
        }
        return pal;
    }
};