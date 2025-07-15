class Solution(object):
    def isValid(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if(len(word)>=3):
            yes=True
        else:
            return False
        digits=[0,1,2,3,4,5,6,7,8,9]
        vowels=['a','e','i','o','u']
        wordd=set(word.lower())
        yes_digit=False
        yes_vow=False
        yes_cons=False
        yes_alpha=False
        count1=0
        count2=0
        count3=0
        print(word)
        for i in wordd:
            if i.isdigit() and count1 <1:
                yes_digit=True
                count1+=1
                continue
            if i in vowels and count2 <1:
                yes_vow=True
                count2+=1
                continue
            if i.lower() not in vowels and count3 <1:
                yes_cons=True
                count3+=1
                continue
        if(count1==0):
            yes_digit=True
        if word.isalnum():
            yes_alpha=True
        else:
            yes_alpha=False
        return yes_digit and yes_vow and yes_cons and yes_alpha
            


          
        